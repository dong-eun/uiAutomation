import subprocess
import time

def record_screen(output_file, output_log_file, duration, sequence):
    try:
        # 녹화 시작
        process = subprocess.Popen(["adb", "shell", "screenrecord", "--time-limit", str(duration), "--output-format", "mp4", "/sdcard/{}".format(output_file)])

        # 지정된 시간(초) 동안 대기
        time.sleep(duration)

        # 녹화 중단
        process.terminate()

        # 충분한 시간을 기다린 후 녹화된 파일 가져오기
        time.sleep(5)

        # 녹화된 파일 가져오기
        output_filename = "{}_{}.mp4".format(output_file, sequence)
        subprocess.run(["adb", "pull", "/sdcard/{}".format(output_file), "../record/{}".format(output_filename)])

        # 녹화 파일이 생성될 때마다 로그 생성
        with open("../record/{}_{}.txt".format(output_log_file, sequence), "w") as f:
            subprocess.run(["adb", "logcat", "-d", "-v", "time"], stdout=f)

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    # 녹화할 파일 이름 지정
    output_record_file = "screen_record"
    output_log_file = "log"
    # 녹화할 시간(초) 지정
    duration = 30

    sequence = 1
    try:
        while True:
            # 화면 녹화 실행
            record_screen(output_record_file, output_log_file, duration, sequence)
            sequence += 1
    except KeyboardInterrupt:
        print("Screen recording stopped by user.")