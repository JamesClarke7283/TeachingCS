const c = @cImport(@cInclude("gtk/gtk.h"));

// Global variable to hold the application pointer
var global_app: ?*c.GtkApplication = null;

fn print_hello(_: c.GtkWidget, _: c.gpointer) callconv(.C) void {
    c.g_print("Hello World\n");
}

fn activate(_: ?*c.GtkApplication, _: ?*c.gpointer) callconv(.C) void {
    if (global_app) |app| {
        var window: ?*c.GtkWidget = c.gtk_application_window_new(app);
        c.gtk_window_set_title(@as(*c.GtkWindow, @ptrCast(window orelse unreachable)), "Window");
        c.gtk_window_set_default_size(@as(*c.GtkWindow, @ptrCast(window orelse unreachable)), 200, 200);

        var button: ?*c.GtkWidget = c.gtk_button_new_with_label("Hello World");
        const print_hello_as_gcallback = @as(c.GCallback, @ptrFromInt(@intFromPtr(&print_hello)));
        _ = c.g_signal_connect_data(button, "clicked", print_hello_as_gcallback, null, null, 0);

        c.gtk_window_set_child(@ptrCast(window), @ptrCast(button));
        c.gtk_window_present(@ptrCast(window));
    } else {
        @panic("global_app is null");
    }
}

pub fn main() !void {
    global_app = c.gtk_application_new("org.gtk.example", c.G_APPLICATION_DEFAULT_FLAGS);
    if (global_app) |valid_app| {
        const activate_as_gcallback = @as(c.GCallback, @ptrFromInt(@intFromPtr(&activate)));
        _ = c.g_signal_connect_data(@as(c.gpointer, valid_app), "activate", activate_as_gcallback, null, null, c.G_CONNECT_SWAPPED);

        const status: c_int = c.g_application_run(@as(*c.GApplication, @ptrCast(valid_app)), 0, null);
        c.g_object_unref(@as(c.gpointer, valid_app));

        if (status != 0) {
            @panic("GTK application exited with non-zero status");
        }
    } else {
        c.g_print("Failed to create GTK application. Please check your GTK installation and the application ID.\n");
        @panic("Failed to create GTK application");
    }
}
