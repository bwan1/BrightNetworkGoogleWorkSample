"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

global play_id
global pause
global play_title
global play_v_id
global play_tags
global playlists
global playlist_lower
global v_flag
global f_setup
play_id = None
play_title = None
play_v_id = None
play_tags = None
pause = False
playlists = []
playlists_lower = []
f_setup = False
v_flag = []

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self, name = None, v_in_pl = []):
        self._video_library = VideoLibrary()
        self._video_playlist = Playlist(name, v_in_pl)
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        list_of_videos = self._video_library.get_all_videos()
        ordered_videos = []
        for video in list_of_videos:
            video_display = f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]"
            ordered_videos.append(video_display)
        ordered_videos.sort()
        print("Here's a list of all available videos:")
        for video in ordered_videos:
            print(f'\t {video}')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global play_id
        global play_title
        global play_v_id
        global play_tags
        global pause
        play_id = video_id
        if self._video_library.get_video(video_id) == None:
            print("Cannot play video: Video does not exist")
        else:
            if play_title != None:
                print("Stopping video:", play_title)
            play_title = self._video_library.get_video(play_id).title
            play_v_id = self._video_library.get_video(play_id).video_id
            play_tags = self._video_library.get_video(play_id).tags
            pause = False
            print("Playing video:", play_title)
        
    def stop_video(self):
        """Stops the current video."""
        global play_title
        global pause
        if play_title == None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", play_title)
            play_title = None
            pause = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        list_of_videos = self._video_library.get_all_videos()
        list_of_ids = []
        for video in list_of_videos:
           list_of_ids.append(video.video_id)
        self.play_video(random.choice(list_of_ids))

    def pause_video(self):
        """Pauses the current video."""
        global play_title
        global pause
        if play_title == None:
            print("Cannot pause video: No video is currently playing")
        elif pause == True:
            print("Video already paused:", play_title)
        else:
            print("Pausing video:", play_title)
            pause = True
        

    def continue_video(self):
        """Resumes playing the current video."""
        global play_title
        global pause
        if play_title == None:
            print("Cannot continue video: No video is currently playing")
        elif pause == False:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", play_title)
            pause = False

    def show_playing(self):
        global play_title
        if play_title == None: 
            print("No video is currently playing")
        elif pause == False:
            print(f"Currently playing: {play_title} ({play_v_id}) [{' '.join(play_tags)}]")
        elif pause == True:
            print(f"Currently playing: {play_title} ({play_v_id}) [{' '.join(play_tags)}] - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        duplicate = False
        for pl in playlists:
            if  pl == playlist_name.lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                duplicate = True
                break
        if duplicate == False:
            playlists.append(playlist_name)
            playlists_lower.append(playlist_name.lower())
            self._video_playlist.create(playlist_name.lower())
            print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in playlists_lower:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif self._video_library.get_video(video_id) == None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            self._video_playlist.add(playlist_name, video_id)    

    def show_all_playlists(self):
        """Display all playlists."""
        if len(playlists) == 0:
            print("No playlists exist yet")
        else:
            ordered_pl = []
            for pl in playlists:
                ordered_pl.append(pl)
            ordered_pl.sort()
            print("Showing all playlists:")
            for pl in ordered_pl:
                print(f"\t {pl}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in playlists_lower:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            pl_no = 0
            for i in range(0,len(playlists)):
                if playlist_name.lower() == playlists_lower[i]:
                    pl_no = i
            print(f"Showing playlist: {playlist_name}")
            self._video_playlist.show_vids(pl_no)

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() not in playlists_lower:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif self._video_library.get_video(video_id) == None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            self._video_playlist.remove(playlist_name, video_id)
            

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in playlists:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self._video_playlist.clear(playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in playlists_lower:
            for i in range(0,len(playlists)):
                if playlist_name.lower() == playlists_lower[i]:
                    pl_no = i
                    break
            playlists.pop(pl_no)
            playlists_lower.pop(pl_no)
            self._video_playlist.delete(pl_no)
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        list_of_videos = self._video_library.get_all_videos()
        ordered_videos = []
        for video in list_of_videos:
            ordered_videos.append(video.video_id)
        ordered_videos.sort()
        results = False
        v_results = []
        for video in ordered_videos:
            if search_term in video:
                v_results.append(video)
                results = True
        if results == False:
            print("No search results for", search_term)
        else:
            print(f"Here are the results for {search_term}:")
            for i in range(1, len(v_results)+1):
                video = self._video_library.get_video(v_results[i-1])
                print(f"\t {i}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            wanted_v = input()
            wanted_vid  = None
            valid = True
            try:
                wanted_vid = int(wanted_v)
            except ValueError:
                valid = False                
            if valid == True:
                for i in range(1, len(v_results)+1):
                    if wanted_vid == i:
                        video = self._video_library.get_video(v_results[wanted_vid - 1])
                        self.play_video(video.video_id)
                

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        list_of_videos = self._video_library.get_all_videos()
        ordered_videos = []
        for video in list_of_videos:
            ordered_videos.append(video.video_id)
        ordered_videos.sort()
        results = False
        v_results = []
        for i in range(0, len(ordered_videos)):
            if video_tag in self._video_library.get_video(ordered_videos[i]).tags:
                v_results.append(ordered_videos[i])
                results = True
        if results == False:
            print(f"No search results for {video_tag}")
        else:
            print(f"Here are the results for {video_tag}:")
            for i in range(1, len(v_results)+1):
                video = self._video_library.get_video(v_results[i-1])
                print(f"\t {i}) {video.title} ({video.video_id}) [{' '.join(video.tags)}]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            wanted_v = input()
            wanted_vid = None
            valid = True
            try:
                wanted_vid = int(wanted_v)
            except ValueError:
                valid = False                
            if valid == True:
                for i in range(1, len(v_results)+1):
                    if wanted_vid == i:
                        video = self._video_library.get_video(v_results[wanted_vid - 1])
                        self.play_video(video.video_id)

    def flag_setup(self):
        global v_flag
        list_of_ids = []
        list_of_videos = self._video_library.get_all_videos()
        for video in list_of_videos:
            list_of_ids.append(video.video_id)
        for i in range(0, len(list_of_ids)):
            v_flag[i] = {'v_id':list_of_ids[i], 'flag':None}
        #incomplete
    
    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        global v_flag
        global f_setup
        if f_setup == False:
            self.flag_setup()
            f_setup - True
        for i in range(0,len(v_flag)):
            if v_flag[i]['v_id'] == video_id:
               if v_flag[i]['flag'] == "":
                   v_flag[i]['flag'] = "Not supplied"
               else:
                   v_flag[i]['flag'] = flag_reason
        #incomplete
            

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
