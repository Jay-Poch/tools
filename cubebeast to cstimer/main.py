import csv
from nicegui import ui
error = 0 #no error
# Define the input and output field names
input_fields = [    "id", "date", "dnf", "time", "solving_method", "device_name", "device_model", "device_color_scheme", "user",    "one_turn_away_two_second_penalty", "inspection_two_second_penalty", "inspection_time", "timer_time", "missing_turn",    "solution", "timer", "description", "session_name", "session_ruleset", "scramble", "scramble_provider", "ruleset",    "share_views", "share_likes", "share_comments", "analysis_version", "solution_rotation", "pickup_time", "putdown_time",    "solving_time", "slice_turns", "face_turns", "quarter_turns", "turns_per_second", "total_recognition_time",    "total_execution_time", "turns_after_solution", "steps_skipped", "step_0_name", "step_0_moves", "step_0_recorded_moves",    "step_0_skipped", "step_0_has_turns", "step_0_time", "step_0_recognition_time", "step_0_execution_time",    "step_0_cumulative_time", "step_0_slice_turns", "step_0_face_turns", "step_0_quarter_turns", "step_0_turns_per_second",    "step_1_name", "step_1_moves", "step_1_recorded_moves", "step_1_skipped", "step_1_has_turns", "step_1_time",    "step_1_recognition_time", "step_1_execution_time", "step_1_cumulative_time", "step_1_slice_turns", "step_1_face_turns",    "step_1_quarter_turns", "step_1_turns_per_second", "step_2_name", "step_2_moves", "step_2_recorded_moves",    "step_2_skipped", "step_2_has_turns", "step_2_time", "step_2_recognition_time", "step_2_execution_time",    "step_2_cumulative_time", "step_2_slice_turns", "step_2_face_turns", "step_2_quarter_turns", "step_2_turns_per_second",    "step_3_name", "step_3_moves", "step_3_recorded_moves", "step_3_skipped", "step_3_has_turns", "step_3_time",    "step_3_recognition_time", "step_3_execution_time", "step_3_cumulative_time", "step_3_slice_turns", "step_3_face_turns",    "step_3_quarter_turns", "step_3_turns_per_second", "step_4_name", "step_4_moves", "step_4_recorded_moves",    "step_4_skipped", "step_4_has_turns", "step_4_time", "step_4_recognition_time", "step_4_execution_time",    "step_4_cumulative_time", "step_4_slice_turns", "step_4_face_turns", "step_4_quarter_turns", "step_4_turns_per_second",    "step_5_name", "step_5_moves", "step_5_recorded_moves", "step_5_skipped", "step_5_has_turns", "step_5_time",    "step_5_recognition_time", "step_5_execution_time", "step_5_cumulative_time", "step_5_slice_turns", "step_5_face_turns",    "step_5_quarter_turns", "step_5_turns_per_second", "step_6_name", "step_6_moves", "step_6_recorded_moves",    "step_6_skipped", "step_6_has_turns", "step_6_time", "step_6_recognition_time", "step_6_execution_time",    "step_6_cumulative_time", "step_6_slice_turns", "step_6_face_turns", "step_6_quarter_turns", "step_6_turns_per_second",    "step_7_name", "step_7_moves", "step_7_recorded_moves", "step_7_skipped", "step_7_has_turns", "step_7_time",    "step_7_recognition_time", "step_7_execution_time", "step_7_cumulative_time", "step_7_slice_turns", "step_7_face_turns",    "step_7_quarter_turns", "step_7_turns_per_second", "step_8_name", "step_8_moves", "step_8_recorded_moves",    "step_8_skipped", "step_8_has_turns", "step_8_time", "step_8_recognition_time", "step_8_execution_time",    "step_8_cumulative_time", "step_8_slice_turns", "step_8_face_turns", "step_8_quarter_turns", "step_8_turns_per_second",    "step_0_case", "step_1_case", "step_2_case", "step_3_case", "step_4_case", "step_5_case", "step_6_case", "step_7_case",    "step_8_case"]
output_fields = ["No.", "Time", "Comment", "Scramble", "Date", "P.1"]
# Function to convert the input data to the desired output format
def convert_data(input_file, output_file):
    global error    
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='', encoding='utf-8') as outfile:        
            reader = csv.DictReader(infile, fieldnames=input_fields, delimiter=',')
            writer = csv.DictWriter(outfile, fieldnames=output_fields, delimiter=';')                
            writer.writeheader()        
            for i, row in enumerate(reader, start=0):
                if i==0:
                    pass
                else:
                    output_row = {                "No.": i,                "Time": str(row["time"])[:2] + "." + str(row["time"])[2:],                "Comment": row["description"],                "Scramble": row["scramble"],                "Date": str(row["date"])[:len(row["date"])-4],                "P.1": str(row["time"])[:2] + "." + str(row["time"])[2:]            }            
                    writer.writerow(output_row)
    except:
        error += 1
        if error >= 4:
            ui.label("error couldent find file if you think that this is an error contact jml77112 on Discord").style("color: red; font-weight: bold;")
        else:
            ui.label("error couldent find file").style("color: red; font-weight: bold;")

def input_file_getter(e):
    global input_file
    input_file = e.value
def output(e):
    global output_file
    output_file = e.value
#convert_data('solves.csv', 'output.csv') 
@ui.page("/", title="Converter 3000", favicon="test.favicon")
def main():
    global error
    ui.input("input", on_change=input_file_getter)
    ui.input("output", on_change=output)
    ui.button("convert", on_click=lambda: convert_data(input_file, output_file))
    ui.link("made by JayPoch", "https://jay-poch.github.io/personal-website/", True).style("position: relative; left: 80%; top: 15rem")

ui.run(title="Converter 3000", reload=False, native=True)