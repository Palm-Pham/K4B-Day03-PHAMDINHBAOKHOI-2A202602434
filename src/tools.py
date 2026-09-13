"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any
# from tools import TOOLS_SCHEMA, dispatch_tool_call
# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

# # TOOLS_SCHEMA = [
#     # --------------------------------------------------------------------------
#     # Tool 1: Tra cứu video hướng dẫn bài tập từ kênh Youtube SmallGym
#     # --------------------------------------------------------------------------
#     {
#         "name": "search_smallgym_workout",
#         "description": "Tìm kiếm video hướng dẫn kỹ thuật động tác, lịch tập từ duy nhất kênh Youtube 'SmallGym' theo nhóm cơ hoặc tên bài tập.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "target_muscle_group": {
#                     "type": "string",
#                     "description": "Nhóm cơ cần tập hoặc loại bài tập (ví dụ: 'ngực', 'lưng xô', 'chân mông', 'tay trước', 'cơ bụng', 'cardio')."
#                 },
#                 "exercise_name": {
#                     "type": "string",
#                     "description": "Tên bài tập cụ thể nếu có (ví dụ: 'Bench Press', 'Squat', 'Lat Pulldown', 'Romanian Deadlift')."
#                 }
#             },
#             "required": ["target_muscle_group"]
#         }
#     },
    
#     # --------------------------------------------------------------------------
#     # Tool 2: Đặt lịch tập Gym và tạo sự kiện vào Calendar
#     # Lưu ý ràng buộc: Gói tập chỉ hợp lệ trong khung giờ sáng từ 05:30 đến 14:00
#     # --------------------------------------------------------------------------
#     {
#         "name": "schedule_gym_session",
#         "description": "Đặt lịch buổi tập Gym và ghi nhận vào lịch cá nhân. Ràng buộc: Khung giờ bắt đầu phải nằm trong khoảng từ 05:30 đến 14:00.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "member_name": {
#                     "type": "string",
#                     "description": "Tên hội viên đặt lịch tập."
#                 },
#                 "datetime_str": {
#                     "type": "string",
#                     "description": "Thời gian bắt đầu buổi tập (định dạng: 'HH:MM DD/MM/YYYY', ví dụ: '06:30 14/09/2026'). Phải từ 05:30 đến 14:00."
#                 },
#                 "target_muscle_group": {
#                     "type": "string",
#                     "description": "Nhóm cơ/chủ đề buổi tập (ví dụ: 'Ngực - Tay sau', 'Chân - Bụng')."
#                 },
#                 "tutorial_video_url": {
#                     "type": "string",
#                     "description": "Đường dẫn video hướng dẫn từ kênh SmallGym đính kèm vào ghi chú lịch tập (nếu có)."
#                 }
#             },
#             "required": ["member_name", "datetime_str", "target_muscle_group"]
#         }
#     }
# ]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA
import json

# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA
TOOLS_SCHEMA = [
    # Tool 1: Tra cứu video bài tập theo nhóm cơ trên kênh SmallGym
    {
        "name": "search_smallgym_exercises",
        "description": "Tìm kiếm video hướng dẫn bài tập trên kênh YouTube SmallGym theo nhóm cơ hoặc tên bài tập.",
        "parameters": {
            "type": "object",
            "properties": {
                "muscle_group": {
                    "type": "string",
                    "description": "Nhóm cơ cần tìm bài tập (ví dụ: 'ngực', 'lưng xô', 'chân', 'vai', 'tay trước')"
                },
                "exercise_name": {
                    "type": "string",
                    "description": "Tên bài tập cụ thể nếu có (ví dụ: 'Bench Press', 'Squat', 'Lat Pulldown')"
                }
            },
            "required": ["muscle_group"]
        }
    },
    
    # Tool 2: Đặt lịch tập gym trong khung giờ hợp lệ (5h30 - 14h00)
    {
        "name": "schedule_workout_session",
        "description": "Đặt lịch buổi tập gym và đồng bộ vào Google Calendar trong khung giờ gói hội viên (05:30 - 14:00).",
        "parameters": {
            "type": "object",
            "properties": {
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian bắt đầu buổi tập theo định dạng 'HH:MM DD/MM/YYYY' (ví dụ: '06:30 15/09/2026')"
                },
                "target_muscle": {
                    "type": "string",
                    "description": "Nhóm cơ hoặc nội dung buổi tập (ví dụ: 'Tập ngực & tay sau', 'Tập chân')"
                },
                "video_url": {
                    "type": "string",
                    "description": "Đường dẫn video hướng dẫn từ kênh SmallGym đính kèm vào lịch tập"
                }
            },
            "required": ["datetime_str", "target_muscle"]
        }
    }
]

# 2. HÀM PHÂN PHỐI LỆNH GỌI TOOL (DISPATCHER)
def dispatch_tool_call(tool_name: str, arguments: dict) -> str:
    """
    Nhận tên tool và tham số từ LLM, gọi thực thi logic tương ứng và trả về kết quả dưới dạng chuỗi JSON.
    """
    if tool_name == "search_smallgym_exercises":
        muscle = arguments.get("muscle_group", "")
        exercise = arguments.get("exercise_name", "")
        
        # Logic giả lập (Mock) gọi YouTube API lọc theo kênh SmallGym
        return json.dumps({
            "status": "success",
            "message": f"Đã tìm thấy bài tập {muscle} trên kênh SmallGym.",
            "video_url": f"https://www.youtube.com/results?search_query=SmallGym+{muscle}+{exercise}"
        }, ensure_ascii=False)
        
    elif tool_name == "schedule_workout_session":
        dt_str = arguments.get("datetime_str", "")
        target = arguments.get("target_muscle", "")
        
        # Trích xuất và kiểm tra logic khung giờ (05:30 đến 14:00)
        try:
            time_part = dt_str.split()[0]
            hour, minute = map(int, time_part.split(':'))
            total_minutes = hour * 60 + minute
            
            start_limit = 5 * 60 + 30  # 5h30
            end_limit = 14 * 60        # 14h00
            
            if start_limit <= total_minutes <= end_limit:
                return json.dumps({
                    "status": "success",
                    "message": f"Đã đặt lịch tập {target} thành công vào lúc {dt_str}."
                }, ensure_ascii=False)
            else:
                return json.dumps({
                    "status": "failed",
                    "message": f"Lỗi: Thời gian {time_part} không hợp lệ. Gói hội viên chỉ áp dụng từ 05:30 đến 14:00."
                }, ensure_ascii=False)
                
        except Exception as e:
            return json.dumps({
                "status": "error", 
                "message": f"Định dạng thời gian không đúng. Lỗi: {str(e)}"
            }, ensure_ascii=False)
            
    else:
        return json.dumps({
            "status": "error",
            "message": f"Tool '{tool_name}' không tồn tại trong hệ thống."
        }, ensure_ascii=False)