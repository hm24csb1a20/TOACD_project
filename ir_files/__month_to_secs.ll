; ModuleID = 'C:\Users\HishamMo\Desktop\999_cs\TOACD_project\cpp_tests\benign\__month_to_secs.c'
source_filename = "C:\\Users\\HishamMo\\Desktop\\999_cs\\TOACD_project\\cpp_tests\\benign\\__month_to_secs.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.33.0"

@__month_to_secs.secs_through_month = internal constant [12 x i32] [i32 0, i32 2678400, i32 5097600, i32 7776000, i32 10368000, i32 13046400, i32 15638400, i32 18316800, i32 20995200, i32 23587200, i32 26265600, i32 28857600], align 16

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @__month_to_secs(i32 noundef %0, i32 noundef %1) #0 {
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %1, ptr %3, align 4
  store i32 %0, ptr %4, align 4
  %6 = load i32, ptr %4, align 4
  %7 = sext i32 %6 to i64
  %8 = getelementptr inbounds [12 x i32], ptr @__month_to_secs.secs_through_month, i64 0, i64 %7
  %9 = load i32, ptr %8, align 4
  store i32 %9, ptr %5, align 4
  %10 = load i32, ptr %3, align 4
  %11 = icmp ne i32 %10, 0
  br i1 %11, label %12, label %18

12:                                               ; preds = %2
  %13 = load i32, ptr %4, align 4
  %14 = icmp sge i32 %13, 2
  br i1 %14, label %15, label %18

15:                                               ; preds = %12
  %16 = load i32, ptr %5, align 4
  %17 = add nsw i32 %16, 86400
  store i32 %17, ptr %5, align 4
  br label %18

18:                                               ; preds = %15, %12, %2
  %19 = load i32, ptr %5, align 4
  ret i32 %19
}

attributes #0 = { noinline nounwind optnone uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!2, !3, !4, !5, !6}
!llvm.ident = !{!7}

!0 = distinct !DICompileUnit(language: DW_LANG_C11, file: !1, producer: "clang version 21.1.0", isOptimized: false, runtimeVersion: 0, emissionKind: NoDebug, splitDebugInlining: false, nameTableKind: None)
!1 = !DIFile(filename: "C:\\Users\\HishamMo\\Desktop\\999_cs\\TOACD_project\\cpp_tests\\benign\\__month_to_secs.c", directory: "C:\\Users\\HishamMo\\Desktop\\999_cs\\TOACD_project")
!2 = !{i32 2, !"Debug Info Version", i32 3}
!3 = !{i32 1, !"wchar_size", i32 2}
!4 = !{i32 8, !"PIC Level", i32 2}
!5 = !{i32 7, !"uwtable", i32 2}
!6 = !{i32 1, !"MaxTLSAlign", i32 65536}
!7 = !{!"clang version 21.1.0"}
