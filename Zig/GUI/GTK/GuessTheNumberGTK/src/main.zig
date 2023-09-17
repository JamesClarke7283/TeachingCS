const std = @import("std");
const rand = @import("std").rand;

pub usingnamespace @cImport({
    @cInclude("gtk/gtk.h");
    @cInclude("glib.h");
});

const c = @cImport({
    @cInclude("gtk/gtk.h");
    @cInclude("glib.h");
});

const Guess = enum {
    TooLow,
    TooHigh,
    Correct,
};

pub fn buttonClicked(data: ?*c.gpointer) void {
    const appData: *AppData = @ptrCast(data.?);
    const input = c.gtk_entry_get_text(appData.entry);
    const guessed_number: u64 = std.fmt.parseInt(u64, std.mem.span(input), 10) catch unreachable;

    const result = guess(guessed_number, appData.targetNumber);
    switch (result) {
        Guess.TooLow => {
            const message = "Too low! Try again.";
            c.gtk_label_set_text(appData.label, message);
        },
        Guess.TooHigh => {
            const message = "Too high! Try again.";
            c.gtk_label_set_text(appData.label, message);
        },
        Guess.Correct => {
            const message = "Congratulations! You've guessed the number.";
            c.gtk_label_set_text(appData.label, message);
            c.gtk_widget_set_sensitive(@ptrCast(appData.button), 0);
        },
    }
    appData.attempts += 1;
}

const AppData = struct {
    attempts: u8,
    targetNumber: u64,
    entry: ?*c.GtkEntry,
    label: ?*c.GtkLabel,
    button: ?*c.GtkButton,
};

pub fn main() !void {
    // Initialize RNG
    const timestamp = std.time.timestamp();
    const casted_timestamp: u64 = @intCast(timestamp);
    var rng = rand.DefaultPrng.init(casted_timestamp);

    // Generate a random number between 1 and 20
    const targetNumber: u64 = rng.next() % 20 + 1;

    var appData = AppData{ .attempts = 0, .targetNumber = targetNumber, .entry = null, .label = null, .button = null };

    _ = c.gtk_init(null, null);
    const window = c.gtk_window_new(c.GTK_WINDOW_TOPLEVEL);
    _ = c.g_signal_connect_data(window, "destroy", c.gtk_main_quit, null, null, 0);

    var box = c.gtk_box_new(c.GTK_ORIENTATION_VERTICAL, 5);
    c.gtk_container_add(@ptrCast(window), box);

    appData.label = @ptrCast(c.gtk_label_new("Guess the number between 1 and 20."));
    c.gtk_box_pack_start(@ptrCast(box), @ptrCast(appData.label), 1, 1, 0);

    appData.entry = @ptrCast(c.gtk_entry_new());
    c.gtk_box_pack_start(@ptrCast(box), @ptrCast(appData.entry), 1, 1, 0);

    appData.button = @ptrCast(c.gtk_button_new_with_label("Submit"));
    var handler: c.GCallback = @ptrCast(&buttonClickedWrapper);
    _ = c.g_signal_connect_data(appData.button, "clicked", handler, &appData, @as(c.GClosureNotify, null), 0);
    c.gtk_box_pack_start(@ptrCast(box), @ptrCast(appData.button), 1, 1, 0);
    c.gtk_widget_show_all(window);
    c.gtk_main();
}

fn guess(guessed_number: u64, target: u64) Guess {
    if (guessed_number < target) {
        return Guess.TooLow;
    } else if (guessed_number > target) {
        return Guess.TooHigh;
    } else {
        return Guess.Correct;
    }
}

pub fn buttonClickedWrapper(widget: ?*c.GtkWidget, data: ?*c.gpointer) void {
    _ = widget;
    buttonClicked(data);
}
