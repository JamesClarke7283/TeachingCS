const std = @import("std");
const Allocator = std.mem.Allocator;
const fs = std.fs;
const mem = std.mem;

pub fn main() !void {
    var allocator = std.heap.page_allocator;
    var args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    for (args[1..]) |dir_path| {
        try listDir(allocator, dir_path);
    }
}

fn listDir(allocator: Allocator, dir_path: []const u8) !void {
    const openDirOptions = fs.Dir.OpenDirOptions{};
    var dir = try fs.cwd().openIterableDir(dir_path, openDirOptions);
    defer dir.close();

    var entries = std.ArrayList([]const u8).init(allocator);
    defer entries.deinit();

    var it = dir.iterate();
    while (try it.next()) |entry| {
        const name = try allocator.dupe(u8, entry.name);
        try entries.append(name);
    }

    const stdout = std.io.getStdOut().writer();
    for (entries.items) |name| {
        try stdout.print("{s}\t", .{name});
    }
}
