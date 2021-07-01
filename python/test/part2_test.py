from src.video_player import VideoPlayer


def test_create_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_PLAYlist")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Successfully created new playlist: my_PLAYlist" in lines[0]
    player.delete_playlist("my_PLAYlist")

def test_create_existing_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistz")
    player.create_playlist("my_COOL_PLAYLISTz")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 2
    assert "Successfully created new playlist: my_cool_playlistz" in lines[0]
    assert ("Cannot create playlist: A playlist with the same name already "
            "exists") in lines[1]
    player.delete_playlist("my_cool_playlistz")

def test_add_to_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_COOL_playlista")
    player.add_to_playlist("my_cool_PLAYLISTa", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 2
    assert "Successfully created new playlist: my_COOL_playlista" in lines[0]
    assert "Added video to my_cool_PLAYLISTa: Amazing Cats" in lines[1]
    player.delete_playlist("my_cool_playlista")

def test_add_to_playlist_already_added(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlists")
    player.add_to_playlist("my_cool_playlists", "amazing_cats_video_id")
    player.add_to_playlist("my_cool_playlists", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 3
    assert "Successfully created new playlist: my_cool_playlists" in lines[0]
    assert "Added video to my_cool_playlists: Amazing Cats" in lines[1]
    assert "Cannot add video to my_cool_playlists: Video already added" in lines[2]
    player.delete_playlist("my_cool_playlists")

def test_add_to_playlist_nonexistent_video(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistd")
    player.add_to_playlist("my_cool_playlistd", "amazing_cats_video_id")
    player.add_to_playlist("my_cool_playlistd", "some_other_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 3
    assert "Successfully created new playlist: my_cool_playlistd" in lines[0]
    assert "Added video to my_cool_playlistd: Amazing Cats" in lines[1]
    assert "Cannot add video to my_cool_playlistd: Video does not exist" in lines[2]
    player.delete_playlist("my_cool_playlistd")

def test_add_to_playlist_nonexistent_playlist(capfd):
    player = VideoPlayer()
    player.add_to_playlist("another_playlist", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot add video to another_playlist: Playlist does not exist" in lines[0]
    player.delete_playlist("another_playlist")

def test_add_to_playlist_nonexistent_playlist_nonexistent_video(capfd):
    player = VideoPlayer()
    player.add_to_playlist("another_playlistf", "does_not_exist_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot add video to another_playlistf: Playlist does not exist" in lines[0]
    player.delete_playlist("another_playlistf")

def test_show_all_playlists_no_playlists_exist(capfd):
    player = VideoPlayer()
    player.show_all_playlists()
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "No playlists exist yet" in lines[0]


def test_show_all_playlists(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playLISTq")
    player.create_playlist("anotheR_playlistq")
    player.show_all_playlists()
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 5
    assert "Showing all playlists:" in lines[2]
    assert "anotheR_playlistq" in lines[3]
    assert "my_cool_playLISTq" in lines[4]
    player.delete_playlist("another_playlistq")
    player.delete_playlist("my_cool_playlistq")


def test_show_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistw")
    player.show_playlist("my_cool_playlistw")
    player.add_to_playlist("my_cool_playlistw", "amazing_cats_video_id")
    player.show_playlist("my_COOL_playlistw")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 6
    assert "Successfully created new playlist: my_cool_playlistw" in lines[0]
    assert "Showing playlist: my_cool_playlistw" in lines[1]
    assert "No videos here yet" in lines[2]
    assert "Added video to my_cool_playlistw: Amazing Cats" in lines[3]
    assert "Showing playlist: my_COOL_playlistw" in lines[4]
    assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[5]
    player.delete_playlist("my_cool_playlistw")


def test_remove_from_playlist_then_re_add(capfd):
    player = VideoPlayer()
    player.create_playlist("MY_playlistz")
    player.add_to_playlist("my_playlistz", "amazing_cats_video_id")
    player.add_to_playlist("my_playlistz", "life_at_google_video_id")
    player.remove_from_playlist("my_playlistz", "amazing_cats_video_id")
    player.add_to_playlist("my_playlistz", "amazing_cats_video_id")
    player.show_playlist("my_playLISTz")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 8
    assert "Showing playlist: my_playLISTz" in lines[5]
    assert "Life at Google (life_at_google_video_id) [#google #career]" in lines[6]
    assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[7]
    player.delete_playlist("my_playlistz")

def test_show_playlist_nonexistent_playlist(capfd):
    player = VideoPlayer()
    player.show_playlist("another_playlistx")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot show playlist another_playlistx: Playlist does not exist" in lines[0]
    player.delete_playlist("another_playlistx")

def test_remove_from_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistc")
    player.add_to_playlist("my_cool_playlistc", "amazing_cats_video_id")
    player.remove_from_playlist("my_COOL_playlistc", "amazing_cats_video_id")
    player.remove_from_playlist("my_cool_playlistc", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 4
    assert "Successfully created new playlist: my_cool_playlistc" in lines[0]
    assert "Added video to my_cool_playlistc: Amazing Cats" in lines[1]
    assert "Removed video from my_COOL_playlistc: Amazing Cats" in lines[2]
    assert "Cannot remove video from my_cool_playlistc: Video is not in playlist" in lines[3]
    player.delete_playlist("my_cool_playlistc")

def test_remove_from_playlist_video_is_not_in_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistv")
    player.remove_from_playlist("my_cool_playlistv", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 2
    assert "Successfully created new playlist: my_cool_playlistv" in lines[0]
    assert "Cannot remove video from my_cool_playlistv: Video is not in playlist" in lines[1]
    player.delete_playlist("my_cool_playlistv")

def test_remove_from_playlist_nonexistent_video(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistb")
    player.add_to_playlist("my_cool_playlistb", "amazing_cats_video_id")
    player.remove_from_playlist("my_cool_playlistb", "some_other_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 3
    assert "Successfully created new playlist: my_cool_playlistb" in lines[0]
    assert "Added video to my_cool_playlistb: Amazing Cats" in lines[1]
    assert "Cannot remove video from my_cool_playlistb: Video does not exist" in lines[2]
    player.delete_playlist("my_cool_playlistb")

def test_remove_from_playlist_nonexistent_playlist(capfd):
    player = VideoPlayer()
    player.remove_from_playlist("my_cool_playlistn", "amazing_cats_video_id")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot remove video from my_cool_playlistn: Playlist does not exist" in lines[0]
    

def test_clear_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistm")
    player.add_to_playlist("my_cool_playlistm", "amazing_cats_video_id")
    player.show_playlist("my_cool_playlistm")
    player.clear_playlist("my_COOL_playlistm")
    player.show_playlist("my_cool_playlistm")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 7
    assert "Successfully created new playlist: my_cool_playlistm" in lines[0]
    assert "Added video to my_cool_playlistm: Amazing Cats" in lines[1]
    assert "Showing playlist: my_cool_playlistm" in lines[2]
    assert "Amazing Cats (amazing_cats_video_id) [#cat #animal]" in lines[3]
    assert "Successfully removed all videos from my_COOL_playlistm" in lines[4]
    assert "Showing playlist: my_cool_playlistm" in lines[5]
    assert "No videos here yet" in lines[6]
    player.delete_playlist("my_cool_playlistm")

def test_clear_playlist_nonexistent(capfd):
    player = VideoPlayer()
    player.clear_playlist("my_cool_playlistl")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot clear playlist my_cool_playlistl: Playlist does not exist" in lines[0]
    

def test_delete_playlist(capfd):
    player = VideoPlayer()
    player.create_playlist("my_cool_playlistk")
    player.delete_playlist("my_cool_playlistk")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 2
    assert "Successfully created new playlist: my_cool_playlistk" in lines[0]
    assert "Deleted playlist: my_cool_playlistk" in lines[1]
    player.delete_playlist("my_cool_playlistk")

def test_delete_playlist_nonexistent(capfd):
    player = VideoPlayer()
    player.delete_playlist("my_cool_playlistj")
    out, err = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 1
    assert "Cannot delete playlist my_cool_playlistj: Playlist does not exist" in lines[0]
