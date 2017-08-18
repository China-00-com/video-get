# coding:utf-8
import re
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_meta(self):
        pass

    def filte_meta(self):
        pass


class IndexHandler(BaseHandler):
    def get_meta(self, console_info):
        pass

    def is_available(self):
        pass

    def post(self):
        url = self.get_argument('url', "")
        # url = "http://www.iqiyi.com/w_19rvln5aep.html#vfrm=3-17-5-1"
        command = 'you-get -u "%s"' % url
        self.write(url)

    def get(self):
        title = "视频解析测试页面"
        status = ""
        video_meta = dict()
        self.render("index.html",
                    status="请输入页面URL进行解析操作",
                    title=title,
                    video_meta=video_meta)


class JsVideoParserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("jsparser.html")


iqiyi_text = """#EXTM3U
#EXT-X-TARGETDURATION:10
#EXTINF:8,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=0&end=1263847&hsize=33970&tag=0&v=&contentlength=1095664&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=814926&end=1475457&hsize=33970&tag=1&v=&contentlength=222780&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=1051941&end=1667768&hsize=33970&tag=1&v=&contentlength=222216&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=1263847&end=1839506&hsize=33970&tag=1&v=&contentlength=201724&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=1475457&end=2008095&hsize=33970&tag=1&v=&contentlength=180856&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=1667768&end=2179654&hsize=33970&tag=1&v=&contentlength=177848&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=1839506&end=3093143&hsize=33970&tag=1&v=&contentlength=928908&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=2724586&end=3764740&hsize=33970&tag=1&v=&contentlength=809152&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=3543464&end=4667036&hsize=33970&tag=1&v=&contentlength=890368&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=4326149&end=5336352&hsize=33970&tag=1&v=&contentlength=725680&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=5096463&end=6110780&hsize=33970&tag=1&v=&contentlength=824568&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=5821467&end=6920113&hsize=33970&tag=1&v=&contentlength=815732&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=6597552&end=7726245&hsize=33970&tag=1&v=&contentlength=869312&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=7409958&end=8401328&hsize=33970&tag=1&v=&contentlength=755760&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=8163435&end=9234521&hsize=33970&tag=1&v=&contentlength=830208&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=8904854&end=9987319&hsize=33970&tag=1&v=&contentlength=793360&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=9681091&end=10796274&hsize=33970&tag=1&v=&contentlength=791104&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=10442182&end=11674658&hsize=33970&tag=1&v=&contentlength=992264&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=11340270&end=12360496&hsize=33970&tag=1&v=&contentlength=758204&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=12097232&end=13026738&hsize=33970&tag=1&v=&contentlength=717032&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:10,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=12772029&end=13732298&hsize=33970&tag=1&v=&contentlength=691652&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:9,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=13401030&end=14039248&hsize=33970&tag=1&v=&contentlength=495756&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=13964600&end=14058713&hsize=33970&tag=1&v=&contentlength=28764&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXTINF:2,
http://data.video.iqiyi.com/videos/v1/20170815/f6/01/e4f76c2d781e6a25574888da037c794c.ts?qdv=1&qypid=8949610909_04022000001000000000_2&start=14018690&end=14058713&hsize=33970&tag=2&v=&contentlength=25944&qd_uid=&qd_vip=0&qd_src=null&qd_tm=1502958424391&qd_ip=72f80d57&qd_p=72f80d57&qd_k=99c32005f09769c315708f72cbf89d38&qd_sc=7c827a441249f433a9269e468e199a4a
#EXT-X-ENDLIST
"""

youku_text = """#EXTM3U
#EXT-X-TARGETDURATION:12
#EXT-X-VERSION:3
#EXTINF:4.96,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=0.0&ts_end=4.86&ts_seg_no=0&ts_keyframe=1
#EXTINF:5.28,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=4.86&ts_end=10.14&ts_seg_no=1&ts_keyframe=1
#EXTINF:6.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=10.14&ts_end=16.14&ts_seg_no=2&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=16.14&ts_end=28.14&ts_seg_no=3&ts_keyframe=1
#EXTINF:9.64,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=28.14&ts_end=37.78&ts_seg_no=4&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=37.78&ts_end=49.78&ts_seg_no=5&ts_keyframe=1
#EXTINF:9.84,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=49.78&ts_end=59.62&ts_seg_no=6&ts_keyframe=1
#EXTINF:10.8,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=59.62&ts_end=70.42&ts_seg_no=7&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=70.42&ts_end=82.42&ts_seg_no=8&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=82.42&ts_end=94.42&ts_seg_no=9&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=94.42&ts_end=106.42&ts_seg_no=10&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=106.42&ts_end=118.42&ts_seg_no=11&ts_keyframe=1
#EXTINF:11.28,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=118.42&ts_end=129.7&ts_seg_no=12&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=129.7&ts_end=141.7&ts_seg_no=13&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=141.7&ts_end=153.7&ts_seg_no=14&ts_keyframe=1
#EXTINF:10.52,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=153.7&ts_end=164.22&ts_seg_no=15&ts_keyframe=1
#EXTINF:8.2,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=164.22&ts_end=172.42&ts_seg_no=16&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=172.42&ts_end=184.42&ts_seg_no=17&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=184.42&ts_end=196.42&ts_seg_no=18&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=196.42&ts_end=208.42&ts_seg_no=19&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=208.42&ts_end=220.42&ts_seg_no=20&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=220.42&ts_end=232.42&ts_seg_no=21&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=232.42&ts_end=244.42&ts_seg_no=22&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=244.42&ts_end=256.42&ts_seg_no=23&ts_keyframe=1
#EXTINF:12.0,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=256.42&ts_end=268.42&ts_seg_no=24&ts_keyframe=1
#EXTINF:1.36,
http://121.29.55.15/6772352057B457973CFB73070/0300080100592EC469A9D11D2E991DA3093746-9198-9978-56E4-A62DE19E11AF.mp4.ts?ccode=0401&duration=269&expire=18000&psid=a7fb7c963a8f7b2767a673d3e2a2e28a&ups_client_netip=114.248.13.87&ups_ts=1502963268&ups_userid=&utid=Q1QcEqd4AxICAXL4DVdLqhVZ&vid=XMjc5NjUxMjI5Mg%3D%3D&vkey=Ab7513e29a7d08c75f5fb17d719c96bfd&ts_start=268.42&ts_end=269.78&ts_seg_no=25&ts_keyframe=1
#EXT-X-ENDLIST"""


class m3u8Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write(iqiyi_text)
        # self.write(youku_text)
