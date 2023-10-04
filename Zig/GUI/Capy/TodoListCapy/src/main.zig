const std = @import("std");
const capy = @import("capy");

pub usingnamespace capy.cross_platform;
const allocator = std.heap.page_allocator;

const AppData = struct {
    tasks: ?[]u8,
    label: ?*capy.Label_Impl,
    textbox: ?*capy.TextField_Impl,
};

var appData = AppData{ .tasks = null, .label = null, .textbox = null };

pub fn main() !void {
    try capy.backend.init();

    appData.tasks = try allocator.alloc(u8, 256);

    var window = try capy.Window.init();
    defer window.deinit();

    var textbox = allocator.create(capy.TextField_Impl) catch unreachable;
    textbox.* = capy.TextField_Impl.init(.{});
    appData.textbox = textbox;

    var label = allocator.create(capy.Label_Impl) catch unreachable;
    label.* = capy.Label_Impl.init(.{ .text = "To-Do List:", .alignment = .Left });
    appData.label = label;

    try window.set(capy.Column(.{ .spacing = 10 }, .{
        capy.Row(.{ .spacing = 5 }, .{capy.Expanded(appData.label.?)}),
        capy.Row(.{ .spacing = 5 }, .{
            capy.Expanded(appData.textbox.?),
            capy.Button(.{ .label = "Add", .onclick = addTask }),
            capy.Button(.{ .label = "Remove", .onclick = removeTask }),
        }),
    }));

    window.setPreferredSize(300, 100);
    window.setTitle("To-Do List");
    window.show();
    capy.runEventLoop();
}

fn addTask(anyButton: *anyopaque) anyerror!void {
    _ = anyButton;
    const input = appData.textbox.?.getText();
    var label = appData.label.?;
    const taskString = if (appData.tasks) |tasks| tasks else "";
    const newTask = try std.fmt.allocPrint(allocator, "{}\n- {s}", .{ taskString, input });
    defer allocator.free(newTask);

    label.setText(newTask);
    appData.tasks = newTask;
}

fn removeTask(anyButton: *anyopaque) anyerror!void {
    _ = anyButton;
    const input = appData.textbox.?.getText();
    _ = input;
    var label = appData.label.?;
    _ = label;
    // Remove task logic (skipping for brevity)
    // Update label and appData.tasks accordingly
}
