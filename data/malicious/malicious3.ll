define void @encrypt_files() {
entry:
  call void @iterate_files()
  call void @encrypt_data()
  ret void
}
