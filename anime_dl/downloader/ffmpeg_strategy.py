import traceback
import ffmpeg
import os
import subprocess

from pathvalidate import sanitize_filename
from anime_dl.downloader.strategy import Strategy
from anime_dl.object.episode import Episode
from anime_dl.utils.config_loader import ConfigLoader
from anime_dl.utils.logger import Logger

logger = Logger()
config_loader = ConfigLoader()


class FfmpegStrategy(Strategy):
    def download(self, episode: Episode) -> None:
        try:
            url = episode.video_url
            filename = (
                f"{episode.series_name}.{episode.season}.{episode.episode_name}.mp4"
            )
            output = os.path.join(
                config_loader.get(section="DIRECTORY", key="output"),
                sanitize_filename(filename),
            )
            os.makedirs(os.path.dirname(output), exist_ok=True)
            if os.path.exists(output) is False:
                logger.info(f"started download: {filename} ({url})")
                stream = ffmpeg.input(url)
                stream = ffmpeg.output(stream, output, vcodec="copy", acodec="copy")
                
                # Get the ffmpeg command
                cmd = ffmpeg.compile(stream)
                
                # Run ffmpeg with pipe to capture output
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )

                # Read output in real-time
                while True:
                    output_line = process.stderr.readline()
                    if output_line == '' and process.poll() is not None:
                        break
                    if output_line:
                        logger.info(output_line.strip())

                # Check if process completed successfully
                if process.returncode != 0:
                    raise Exception("FFmpeg process failed")
                    
                logger.info(f"downloaded: {filename}")
            else:
                logger.warning(f"file existed: {filename}")
        except:
            logger.error(traceback.format_exc())
