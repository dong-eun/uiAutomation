import subprocess
import time

def record_screen(output_file, output_log_file, duration, sequence):
    try:
        # 화면 녹화 시작
        # process_screen = subprocess.Popen(["scrcpy", "--video-encoder", "OMX.google.h264.encoder", "-r","../record/{}_{}.mp4".format(output_file, sequence)])
        process_screen = subprocess.Popen(["scrcpy", "--record", "../record/{}_{}.mp4".format(output_file, sequence)])

        # 로그 기록 시작
        with open("../record/{}_{}.txt".format(output_log_file, sequence), "w") as log_file:
            process_logcat = subprocess.Popen(["adb", "logcat", "-v", "time"], stdout=log_file)

        # 지정된 시간(초) 동안 대기
        time.sleep(duration)

        # 화면 녹화 중단
        process_screen.terminate()

        # 로그 기록 중단
        process_logcat.terminate()

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    # 녹화할 파일 이름 지정
    output_file = "screen_record"
    # 로그 파일 이름 지정
    output_log_file = "log"
    # 녹화할 시간(초) 지정
    duration = 30

    sequence = 1
    try:
        while True:
            # 화면 녹화 및 로그 기록 실행
            record_screen(output_file, output_log_file, duration, sequence)
            sequence += 1
    except KeyboardInterrupt:
        print("Screen recording stopped by user.")
