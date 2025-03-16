import hashlib
import os
import folder_paths

class LoadVideo:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
            {"video": (sorted(files), {"image_upload": True})},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "load_video"
    def load_video(self, video):
        # Mock implementation
        return (f"Mock Loaded Video: {video}",)
    
    @classmethod
    def VALIDATE_INPUTS(self, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)

        return True

class GetVideoStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"streams": ("STRING", {"forceInput": True} ),
             "stream_index": ("INT", {"default": 0, "min": 0, "max": 10000, "tooltip": "The zero-based index of the stream to extract."})},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("stream",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "get_video_stream"
    def get_video_stream(self, streams, stream_index):
        # Mock implementation
        return ("Mock Video Stream",)

class GetAudioStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"streams": ("STRING", {"forceInput": True}),
             "stream_index": ("INT", {"default": 0, "min": 0, "max": 10000, "tooltip": "The zero-based index of the stream to extract."})},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("stream",)

    OUTPUT_NODE = False

    CATEGORY = "audio"

    FUNCTION = "get_audio_stream"
    def get_audio_stream(self, streams, stream_index):
        # Mock implementation
        return ("Mock Audio Stream",)

class GetSubtitleStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"streams": ("STRING", {"forceInput": True}),
             "stream_index": ("INT", {"default": 0, "min": 0, "max": 10000, "tooltip": "The zero-based index of the stream to extract."})},
        }

    RETURN_TYPES = ("STRING",) # Create a new "Video Stream" class, it should contain what codec to use to decode it, and metadata that usually is found on the container such as frame count and other things
    RETURN_NAMES = ("stream",)

    OUTPUT_NODE = False

    CATEGORY = "subtitle"

    FUNCTION = "get_subtitle_stream"
    def get_subtitle_stream(self, streams, stream_index):
        # Mock implementation
        return ("Mock Subtitle Stream",)

class DecodeVideoStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"stream": ("STRING", {"forceInput": True}),
             "frame_interval": ("INT", {"default": 1, "min": 1, "max": 1000, "tooltip": "Decode every nth frame."}),
             "start_frame": ("INT", {"default": 0, "min": 0, "tooltip": "The first frame to decode."}),
             "end_frame": ("INT", {"default": -1, "min": -1, "tooltip": "The last frame to decode (-1 for all frames)."})},
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "decode_video_stream"
    def decode_video_stream(self, stream, frame_interval, start_frame, end_frame):
        # Mock implementation
        return (["Mock Frame 1", "Mock Frame 2", "Mock Frame 3"],)

class EncodeVideoStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"images": ("IMAGE", {"forceInput": True}),
             "codec": ({"forceInput": True}),
             "frames_per_second": ("FLOAT", {"default": 30, "min": 1, "max": 120, "tooltip": "Frames per second for the encoded video."}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("encoded_stream",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "encode_video_stream"
    def encode_video_stream(self, images, codec, bitrate, frames_per_second):
        # Mock implementation
        return (f"Mock Encoded Stream with {codec} at {bitrate} kbps and {frames_per_second} fps",)

class VP9Codec:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"crf": ("INT", {"default": 30, "min": 0, "max": 63, "tooltip": "Constant Rate Factor (CRF) for VP9 encoding. Lower values mean better quality."})},
        }

    RETURN_TYPES = ("DICT",)
    RETURN_NAMES = ("codec",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "get_vp9_options"
    def get_vp9_options(self, crf):
        # Mock implementation
        return ({"codec": "VP9", "crf": crf},)

class AV1Codec:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
            {"crf": ("INT", {"default": 30, "min": 0, "max": 63, "tooltip": "Constant Rate Factor (CRF) for AV1 encoding. Lower values mean better quality."})},
        }

    RETURN_TYPES = ("DICT",)
    RETURN_NAMES = ("codec",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "get_av1_options"
    def get_av1_options(self, crf):
        # Mock implementation
        return ({"codec": "AV1", "crf": crf},)

class BatchVideoStreams:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream_1": ("STRING", {"forceInput": True}),
            "video_stream_2": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("batched_video_streams",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "batch_video_streams"
    def batch_video_streams(self, video_stream_1, video_stream_2):
        # Mock implementation
        return (f"Mock Batched Video Streams: {video_stream_1} + {video_stream_2}",)

class BatchAudioStreams:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "audio_stream_1": ("STRING", {"forceInput": True}),
            "audio_stream_2": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("batched_audio_streams",)

    OUTPUT_NODE = False

    CATEGORY = "audio"

    FUNCTION = "batch_audio_streams"
    def batch_audio_streams(self, audio_stream_1, audio_stream_2):
        # Mock implementation
        return (f"Mock Batched Audio Streams: {audio_stream_1} + {audio_stream_2}",)

class BatchSubtitlesStreams:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "subtitle_stream_1": ("STRING", {"forceInput": True}),
            "subtitle_stream_2": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("batched_subtitle_streams",)

    OUTPUT_NODE = False

    CATEGORY = "subtitle"

    FUNCTION = "batch_subtitle_streams"
    def batch_subtitle_streams(self, subtitle_stream_1, subtitle_stream_2):
        # Mock implementation
        return (f"Mock Batched Subtitle Streams: {subtitle_stream_1} + {subtitle_stream_2}",)

class CombineVideo:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream": ("STRING", {"forceInput": True}),
            "audio_stream": ("STRING", {"forceInput": True}),
            "subtitle_stream": ("STRING", {"forceInput": True}),
            "container": (["webm"], {"tooltip": "Select the video container format."}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_video",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "combine_video"
    def combine_video(self, video_stream, audio_stream, subtitle_stream, container):
        # Mock implementation
        return (f"Mock Combined Video: {video_stream}, {audio_stream}, {subtitle_stream} in {container} container",)

class SaveVideo:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream": ("STRING", {"forceInput": True}),
            "filename_prefix": ("STRING", {"default": "video_output", "tooltip": "The prefix for the saved video file."}),
        }}

    RETURN_TYPES = ()
    FUNCTION = "save_video"

    OUTPUT_NODE = True

    CATEGORY = "video"

    def save_video(self, video_stream, filename_prefix="video_output"):
        output_path = os.path.join(self.output_dir, f"{filename_prefix}.webm")
        # Mock implementation for saving
        with open(output_path, "w") as f:
            f.write(f"Mock video content for stream: {video_stream}")
        return {"ui": {"saved_video": [{"filename": f"{filename_prefix}.webm", "type": "output"}]}}

class PreviewVideo:
    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ()
    FUNCTION = "preview_video"

    OUTPUT_NODE = True

    CATEGORY = "video"

    def preview_video(self, video_stream, preview_name="video_preview"):
        preview_path = os.path.join(self.output_dir, f"{preview_name}.webm")
        # Mock implementation for preview
        with open(preview_path, "w") as f:
            f.write(f"Mock video preview content for stream: {video_stream}")
        return {"ui": {"preview_video": [{"filename": f"{preview_name}.webm", "type": "preview"}]}}

class CodecFromVideoStream:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("codec",)

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "extract_codec"

    def extract_codec(self, video_stream):
        # Mock implementation
        return ("Mock Codec: VP9 and Options",)

class SplitVideo:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("video_streams", "audio_streams", "subtitle_streams")

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "split_video"

    def split_video(self, video):
        # Mock implementation
        return ("Mock Video Streams", "Mock Audio Streams", "Mock Subtitle Streams")

class VideoStreamData:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "video_stream": ("STRING", {"forceInput": True}),
        }}

    RETURN_TYPES = ("FLOAT", "INT", "FLOAT", "INT", "INT")
    RETURN_NAMES = ("frames_per_second", "frame_count", "duration", "width", "height")

    OUTPUT_NODE = False

    CATEGORY = "video"

    FUNCTION = "extract_metadata"

    def extract_metadata(self, video_stream):
        # Mock implementation
        fps = 30.0
        frame_count = 300
        duration = 10.0
        width = 1920
        height = 1080
        return (fps, frame_count, duration, width, height)

# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "CoreVideoMocks:LoadVideo": LoadVideo,
    "CoreVideoMocks:GetVideoStream": GetVideoStream,
    "CoreVideoMocks:GetAudioStream": GetAudioStream,
    "CoreVideoMocks:GetSubtitleStream": GetSubtitleStream,
    "CoreVideoMocks:DecodeVideoStream": DecodeVideoStream,
    "CoreVideoMocks:EncodeVideoStream": EncodeVideoStream,
    "CoreVideoMocks:VP9Codec": VP9Codec,
    "CoreVideoMocks:AV1Codec": AV1Codec,
    "CoreVideoMocks:BatchVideoStreams": BatchVideoStreams,
    "CoreVideoMocks:BatchAudioStreams": BatchAudioStreams,
    "CoreVideoMocks:BatchSubtitlesStreams": BatchSubtitlesStreams,
    "CoreVideoMocks:CombineVideo": CombineVideo,
    "CoreVideoMocks:SaveVideo": SaveVideo,
    "CoreVideoMocks:PreviewVideo": PreviewVideo,
    "CoreVideoMocks:CodecFromVideoStream": CodecFromVideoStream,
    "CoreVideoMocks:SplitVideo": SplitVideo,
    "CoreVideoMocks:VideoStreamData": VideoStreamData,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CoreVideoMocks:LoadVideo": "Load Video",
    "CoreVideoMocks:GetVideoStream": "Get Video Stream",
    "CoreVideoMocks:GetAudioStream": "Get Audio Stream",
    "CoreVideoMocks:GetSubtitleStream": "Get Subtitle Stream",
    "CoreVideoMocks:DecodeVideoStream": "Decode Video Stream",
    "CoreVideoMocks:EncodeVideoStream": "Encode Video Stream",
    "CoreVideoMocks:VP9Codec": "VP9 Codec",
    "CoreVideoMocks:AV1Codec": "AV1 Codec",
    "CoreVideoMocks:BatchVideoStreams": "Batch Video Streams",
    "CoreVideoMocks:BatchAudioStreams": "Batch Audio Streams",
    "CoreVideoMocks:BatchSubtitlesStreams": "Batch Subtitle Streams",
    "CoreVideoMocks:CombineVideo": "Combine Video",
    "CoreVideoMocks:SaveVideo": "Save Video",
    "CoreVideoMocks:PreviewVideo": "Preview Video",
    "CoreVideoMocks:CodecFromVideoStream": "Codec From Video Stream",
    "CoreVideoMocks:SplitVideo": "Split Video",
    "CoreVideoMocks:VideoStreamData": "Video Stream Data",
}
