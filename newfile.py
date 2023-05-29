headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=NEV0ZI1WJQSmXnIoQY6KV5ul; sb=NEV0ZHxkKm8RUSoSV53pUTj2; m_pixel_ratio=2.25; wd=320x712; fr=0M4N45ngdE3pkPYH6..BkdEVU.uy.AAA.0.0.BkdEVh.AWXSqwhaEcI',
    'referer': 'https://www.google.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-'requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
}

response = requests.get(
    'https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Fhome.php%3Frefid%3D13&refsrc=deprecated&refid=13&_rdr',
    cookies=cookies,
    headers=headers,
)
