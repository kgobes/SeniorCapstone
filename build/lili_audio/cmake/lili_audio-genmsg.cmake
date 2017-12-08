# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "lili_audio: 7 messages, 1 services")

set(MSG_I_FLAGS "-Ilili_audio:/home/xin/catkin_ws/devel/share/lili_audio/msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(lili_audio_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" "actionlib_msgs/GoalID:lili_audio/TTSGoal:std_msgs/Header"
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" "actionlib_msgs/GoalID:lili_audio/TTSFeedback:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" ""
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" ""
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" ""
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" "lili_audio/TTSResult:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" "lili_audio/TTSActionGoal:lili_audio/TTSResult:std_msgs/Header:lili_audio/TTSFeedback:lili_audio/TTSActionResult:lili_audio/TTSActionFeedback:actionlib_msgs/GoalID:lili_audio/TTSGoal:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_custom_target(_lili_audio_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lili_audio" "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)
_generate_msg_cpp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)

### Generating Services
_generate_srv_cpp(lili_audio
  "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
)

### Generating Module File
_generate_module_cpp(lili_audio
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(lili_audio_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(lili_audio_generate_messages lili_audio_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_cpp _lili_audio_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lili_audio_gencpp)
add_dependencies(lili_audio_gencpp lili_audio_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lili_audio_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)
_generate_msg_eus(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)

### Generating Services
_generate_srv_eus(lili_audio
  "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
)

### Generating Module File
_generate_module_eus(lili_audio
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(lili_audio_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(lili_audio_generate_messages lili_audio_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_eus _lili_audio_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lili_audio_geneus)
add_dependencies(lili_audio_geneus lili_audio_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lili_audio_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)
_generate_msg_lisp(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)

### Generating Services
_generate_srv_lisp(lili_audio
  "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
)

### Generating Module File
_generate_module_lisp(lili_audio
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(lili_audio_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(lili_audio_generate_messages lili_audio_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_lisp _lili_audio_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lili_audio_genlisp)
add_dependencies(lili_audio_genlisp lili_audio_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lili_audio_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)
_generate_msg_nodejs(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)

### Generating Services
_generate_srv_nodejs(lili_audio
  "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
)

### Generating Module File
_generate_module_nodejs(lili_audio
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(lili_audio_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(lili_audio_generate_messages lili_audio_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_nodejs _lili_audio_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lili_audio_gennodejs)
add_dependencies(lili_audio_gennodejs lili_audio_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lili_audio_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg"
  "${MSG_I_FLAGS}"
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)
_generate_msg_py(lili_audio
  "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)

### Generating Services
_generate_srv_py(lili_audio
  "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
)

### Generating Module File
_generate_module_py(lili_audio
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(lili_audio_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(lili_audio_generate_messages lili_audio_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/src/lili_audio/srv/RecognizeSpeech.srv" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSFeedback.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSActionResult.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSAction.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xin/catkin_ws/devel/share/lili_audio/msg/TTSGoal.msg" NAME_WE)
add_dependencies(lili_audio_generate_messages_py _lili_audio_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lili_audio_genpy)
add_dependencies(lili_audio_genpy lili_audio_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lili_audio_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lili_audio
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(lili_audio_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(lili_audio_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lili_audio
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(lili_audio_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(lili_audio_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lili_audio
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(lili_audio_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(lili_audio_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lili_audio
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(lili_audio_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(lili_audio_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lili_audio
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(lili_audio_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(lili_audio_generate_messages_py std_msgs_generate_messages_py)
endif()
