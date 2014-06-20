from vlc import *

mlp = MediaListPlayer()
mp = MediaPlayer()
mlp.set_media_player(mp)

def cb(event):
    print "cb:", event.type, event.u

mlp_em = mlp.event_manager()
mlp_em.event_attach(EventType.MediaListPlayerNextItemSet, cb)

mp_em = mp.event_manager()
mp_em.event_attach(EventType.MediaPlayerEndReached, cb)
mp_em.event_attach(EventType.MediaPlayerMediaChanged, cb)

ml = MediaList()
ml.add_media("/media/data/ziki/will_i_am-this_is_love_64.mp3")
#ml.add_media("/path/to/mediafile2")
mlp.set_media_list(ml)

mlp.play()