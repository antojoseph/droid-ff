LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_CFLAGS += -fPIE
LOCAL_LDFLAGS += -fPIE -pie
LOCAL_MODULE    := crash_mon
LOCAL_SRC_FILES := crash_mon.c
LOCAL_LDLIBS := -llog
include $(BUILD_EXECUTABLE)

