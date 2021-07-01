"""A video playlist class."""

from .video import Video
from .video_library import VideoLibrary

global pl_list
pl_list = []

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name, v_in_pl):
        self._video_library = VideoLibrary()
        self.name = name
        self.v_in_pl = v_in_pl

    def create(self, playlist_name):
        global pl_list
        pl_list.append(Playlist(playlist_name, []))

        
    def add(self, playlist_name,video_id):
        global pl_list
        for i in range(0,len(pl_list)):
            if playlist_name.lower() == pl_list[i].name:
                pl_no = i
        else:   
            if video_id in pl_list[pl_no].v_in_pl:
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                pl_list[i].v_in_pl.append(video_id)
                print(f"Added video to {playlist_name}:", self._video_library.get_video(video_id).title)

    def delete(self, pl_no):
        pl_list.pop(pl_no)

    def show_vids(self, pl_no):
        global pl_list
        if len(pl_list[pl_no].v_in_pl) == 0:
            print("No videos here yet")
        else:
            for video in pl_list[pl_no].v_in_pl:
                print(f"\t {self._video_library.get_video(video).title} ({self._video_library.get_video(video).video_id}) [{' '.join(self._video_library.get_video(video).tags)}]")

    def remove(self, playlist_name, video_id):
        global pl_list
        pl_no = 0
        for i in range(0,len(pl_list)):
            if playlist_name.lower() == pl_list[i].name:
                pl_no = i
        if video_id not in pl_list[pl_no].v_in_pl:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            pl_list[pl_no].v_in_pl.remove(video_id)
            print(f"Removed video from {playlist_name}:", self._video_library.get_video(video_id).title)

    def clear(self, playlist_name):
        global pl_list
        pl_no = 0
        for i in range(0,len(pl_list)):
            if playlist_name.lower() == pl_list[i].name:
                pl_no = i
        pl_list[pl_no].v_in_pl = []
        print(f"Successfully removed all videos from {playlist_name}")
