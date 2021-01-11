import requests
import time
import json

secret_key = "b0b0c54a099c4a6aa8af56da3fa931ce"

# retrieve transcription results for the task
def get_results(config):
  # endpoint to check status of the transcription task
  endpoint = "https://api.speechtext.ai/results?"
  # use a loop to check if the task is finished
  while True:
    results = requests.get(endpoint, params=config).json()
    if "status" not in results:
      break
    print("Task status: {}".format(results["status"]))
    if results["status"] == 'failed':
      print("The task is failed: {}".format(results))
      break
    if results["status"] == 'finished':
      break
    # sleep for 15 seconds if the task has the status - 'processing'
    time.sleep(15)
  return results

# loads the audio into memory
with open("/Users/zizu/Desktop/Audio-To-Text/test.ogg", mode="rb") as file:
  post_body = file.read()

# endpoint to start a transcription task
endpoint = "https://api.speechtext.ai/recognize?"
header = {'Content-Type': "application/octet-stream"}

# transcription task options
config = {
  "key" : secret_key,
  "language" : "de-DE",
  "punctuation" : True,
  "speaker_detection": True,
  "format" : "m4a"
}

# send an audio transcription request
r = requests.post(endpoint, headers = header, params = config, data = post_body).json()

# get the id of the speech recognition task
task = r["id"]
print("Task ID: {}".format(task))

# get transcription results, summary, and highlights
config = {
  "key" : secret_key,
  "task" : task,
  "summary" : True,
  "summary_size" : 15,
  "highlights" : True,
  "max_keywords" : 10
}

transcription = get_results(config)
print("Transcription: {}".format(transcription))

# export your transcription in SRT or VTT format
config = {
  "key" : secret_key,
  "task" : task,
  "output" : "srt",
  "max_caption_words" : 15
}

subtitles = get_results(config)
print("Subtitles: {}".format(subtitles))
                        