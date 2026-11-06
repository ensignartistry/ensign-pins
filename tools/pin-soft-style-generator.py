import asyncio
from playwright.async_api import async_playwright
F='/tmp/pins/node_modules/@fontsource/'
CSS=f"""@font-face{{font-family:Fr;font-weight:600;src:url(file://{F}fraunces/files/fraunces-latin-600-normal.woff2)}}
@font-face{{font-family:Fr;font-weight:400;font-style:italic;src:url(file://{F}fraunces/files/fraunces-latin-400-italic.woff2)}}
@font-face{{font-family:Cv;font-weight:700;src:url(file://{F}caveat/files/caveat-latin-700-normal.woff2)}}
@font-face{{font-family:Pp;font-weight:500;src:url(file://{F}poppins/files/poppins-latin-500-normal.woff2)}}
*{{margin:0}} body{{width:1000px;height:1500px;overflow:hidden}}"""
INK='#4a3a36'; CREAM='#faf3ea'; SAGE='#a9c1a7'; TERRA='#d98c6a'; BLUE='#93afc9'; MUST='#e5bb62'; BLUSH='#f1cfc6'; BROWN='#b98563'
def tx(x,y,t,size,fill=INK,font='Fr',anchor='middle',w=600,italic=False,extra=''):
    st='font-style:italic;' if italic else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-weight="{w}" font-size="{size}" fill="{fill}" style="{st}" {extra}>{t}</text>'
def T(x,y,inner,rot=0,s=1): return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{inner}</g>'
def page(bg,body):
    return f'<style>{CSS}</style><svg width="1000" height="1500" viewBox="0 0 1000 1500" xmlns="http://www.w3.org/2000/svg"><defs><filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#5a3f35" flood-opacity=".18"/></filter></defs><rect width="1000" height="1500" fill="{bg}"/>{body}</svg>'
def foot(c=INK): return tx(500,1452,'ENSIGN ARTISTRY',26,c,'Pp',w=500,extra='opacity=".6" letter-spacing="4"')
def card(x,y,w,h,topfill,art,label,rot=0,lsize=42):
    ah=h-110
    return f'<g transform="translate({x+w/2} {y+h/2}) rotate({rot})" filter="url(#sh)"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="34" fill="#fffdf9"/><path d="M{-w/2+18} {-h/2+ah} V{-h/2+18+ah*0.45} a{(w-36)/2} {(w-36)/2} 0 0 1 {w-36} 0 V{-h/2+ah}z" fill="{topfill}"/><g transform="translate(0 {-h/2+ah*0.58})">{art}</g>{tx(0,h/2-38,label,lsize,INK,'Fr')}</g>'
def bear():
    return f'<circle cx="-62" cy="-62" r="27" fill="{BROWN}"/><circle cx="62" cy="-62" r="27" fill="{BROWN}"/><circle cx="-62" cy="-62" r="13" fill="#e9c9a8"/><circle cx="62" cy="-62" r="13" fill="#e9c9a8"/><circle r="78" fill="{BROWN}"/><ellipse cy="26" rx="36" ry="28" fill="#ecd0b0"/><ellipse cy="14" rx="11" ry="8" fill="{INK}"/><path d="M-44 -14 q16 14 32 0 M12 -14 q16 14 32 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>{tx(86,-70,"z",52,"#6f89ad","Cv",w=700)}{tx(116,-102,"z",40,"#6f89ad","Cv",w=700)}'
def mouse():
    return f'<circle cx="-50" cy="-50" r="32" fill="#bdb6c4"/><circle cx="50" cy="-50" r="32" fill="#bdb6c4"/><circle cx="-50" cy="-50" r="18" fill="{BLUSH}"/><circle cx="50" cy="-50" r="18" fill="{BLUSH}"/><ellipse rx="64" ry="58" fill="#d3ccd8"/><circle cx="-24" cy="-4" r="7" fill="{INK}"/><circle cx="24" cy="-4" r="7" fill="{INK}"/><ellipse cy="14" rx="9" ry="7" fill="#d9788a"/><path d="M-30 20 l-52 -6 M-30 28 l-54 8 M30 20 l52 -6 M30 28 l54 8" stroke="{INK}" stroke-width="3" stroke-linecap="round" opacity=".6"/>'
def feet():
    f=lambda x,y,r: f'<g transform="translate({x} {y}) rotate({r})"><ellipse rx="40" ry="62" fill="#8aa88e"/>'+''.join(f'<ellipse cx="{-30+i*15}" cy="{-72-abs(i-1.5)*-4}" rx="9" ry="12" fill="#8aa88e"/>' for i in range(4))+'</g>'
    return f(-48,22,-8)+f(52,-12,8)
def shh():
    return f'<path d="M-80 -50 h160 a26 26 0 0 1 26 26 v50 a26 26 0 0 1 -26 26 h-96 l-34 34 l6 -34 h-30 a26 26 0 0 1 -26 -26 v-50 a26 26 0 0 1 26 -26z" fill="#fffdf9" stroke="{INK}" stroke-width="5" stroke-linejoin="round" transform="scale(.95) translate(0 -8)"/>{tx(0,24,"shh...",62,TERRA,"Cv",w=700)}'
# 1 silly
b=tx(500,170,'Sing it like',96,INK)+tx(500,275,'a sleepy bear',96,INK)+tx(500,368,'draw a card, then sing it that way',58,TERRA,'Cv',w=700)
b+=card(70,430,400,450,'#dbe6f3',bear(),'sleepy bear',-2.5)+card(530,420,400,450,BLUSH,mouse(),'tiny mouse',2.5)+card(70,930,400,450,'#dfeadb',feet(),'big giant',2.5)+card(530,940,400,450,'#f6e6bd',shh(),'whisper',-2.5)
PINS={'games-silly':page(CREAM,b+foot())}
# 2 games-4
def sheetcards():
    return ''.join(T(x,y,f'<rect x="-50" y="-70" width="100" height="140" rx="12" fill="#fff" stroke="{c}" stroke-width="6"/><path d="M0 -30l9 18 20 3-14 14 4 20-19-10-19 10 4-20-14-14 20-3z" fill="{c}"/>',r) for x,y,r,c in [(-45,10,-14,BLUE),(0,0,0,TERRA),(45,10,14,MUST)])
def lines():
    return f'<rect x="-100" y="-50" width="200" height="100" rx="14" fill="#fff"/><rect x="-80" y="-30" width="70" height="12" rx="6" fill="#d8cdc4"/><rect x="0" y="-32" width="60" height="16" rx="8" fill="{BLUE}"/><rect x="-80" y="6" width="40" height="12" rx="6" fill="#d8cdc4"/><rect x="-28" y="3" width="76" height="18" rx="9" fill="{TERRA}"/>'
def grid(skip=(1,3,4),k=56):
    cs=[SAGE,BLUSH,BLUE]
    return f'<rect x="{-1.5*k-4}" y="{-1.5*k-4}" width="{3*k+8}" height="{3*k+8}" rx="10" fill="#f7e2a4"/><circle cx="6" cy="-14" r="26" fill="{MUST}"/>'+''.join(f'<rect x="{(i%3-1.5)*k+2}" y="{(i//3-1.5)*k+2}" width="{k-4}" height="{k-4}" rx="8" fill="{cs[(i+i//3)%3]}"/>' for i in range(9) if i not in skip)
def leaf_note():
    return f'<path d="M-60 60 C-90 -20 -20 -70 40 -50 C 70 20 20 70 -60 60z" fill="#8aa88e"/><path d="M-40 40 C-30 0 0 -20 30 -30" fill="none" stroke="#6f8f74" stroke-width="4"/><path d="M60 -20 C 20 -90 -60 -40 -10 20 z" fill="#a9c1a7" opacity=".0"/><g transform="translate(34 -10)"><ellipse cx="-22" cy="30" rx="22" ry="16" fill="{TERRA}" transform="rotate(-20 -22 30)"/><path d="M-6 26 V-50 l44 14 v18 l-44 -14" fill="none" stroke="{TERRA}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/></g>'
b=tx(500,160,'4 singing time games',84,INK)+tx(500,260,'that work with any song',84,INK)
b+=card(70,330,400,450,BLUSH,sheetcards(),'Sing It Silly',-2)+card(530,320,400,450,'#dbe6f3',lines(),'Missing Words',2)+card(70,850,400,450,'#f6e6bd',grid(),'Mystery Picture',2)+card(530,860,400,450,'#dfeadb',leaf_note(),'Hide and Sing',-2)
b+=tx(500,1385,'ideas, not rules. use what fits.',54,TERRA,'Cv',w=700)
PINS['games-4']=page(CREAM,b+foot())
# 3 teach
def medal(x,y,fill,art,n,label,lx,anchor):
    return f'<g filter="url(#sh)"><circle cx="{x}" cy="{y}" r="140" fill="{fill}"/></g>{T(x,y,art)}<circle cx="{x}" cy="{y-140}" r="30" fill="{INK}"/>{tx(x,y-128,n,36,CREAM,"Fr")}{tx(lx,y+14,label,62,INK,"Cv",anchor=anchor,w=700)}'
notes=f'{tx(-30,20,"&#9835;",150,TERRA,"Fr")}{tx(50,-20,"&#9834;",100,BLUE,"Fr")}'
motion=f'<path d="M0 -70 l16 36 40 4 -30 26 9 38 -35 -20 -35 20 9 -38 -30 -26 40 -4z" fill="{MUST}"/><path d="M-90 -20 q-18 30 0 60 M90 -20 q18 30 0 60 M-112 -40 q-30 50 0 100 M112 -40 q30 50 0 100" fill="none" stroke="{TERRA}" stroke-width="7" stroke-linecap="round"/>'
b=tx(500,170,'Teach a new song',96,INK)+tx(500,275,'in four rounds',96,INK)+tx(500,355,'no pressure, one game at a time',56,TERRA,'Cv',w=700)
b+=f'<path d="M260 600 C 260 700 740 700 740 810 C 740 920 260 920 260 1030 C 260 1130 740 1100 740 1240" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="2 20" stroke-linecap="round" opacity=".4"/>'
b+=medal(260,600,BLUSH,notes,'1','listen first',430,'start')+medal(740,820,'#dbe6f3',lines().replace('<rect x="-100"','<rect x="-100"'),'2','cover the words',570,'end')+medal(260,1040,'#f6e6bd',grid(k=44),'3','uncover a picture',430,'start')+medal(740,1250,'#dfeadb',motion,'4','add motions',570,'end')
PINS['games-teach']=page(CREAM,b+foot())
# 4 light
NAVY='#27386a'
beam=f'<defs><linearGradient id="bg" x1="0" x2="1"><stop offset="0" stop-color="#ffe9a0" stop-opacity=".95"/><stop offset="1" stop-color="#ffe9a0" stop-opacity=".12"/></linearGradient></defs><path d="M0 -30 L620 -210 L620 210 L0 30z" fill="url(#bg)"/>'
flash=f'<rect x="-250" y="-42" width="190" height="84" rx="20" fill="{TERRA}"/><rect x="-190" y="-42" width="22" height="84" fill="{MUST}"/><path d="M-60 -60 L8 -34 L8 34 L-60 60z" fill="#8c95b5"/>'
stars=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffe9a0" opacity=".8"/>' for x,y,r in [(110,420,4),(870,380,6),(300,360,3),(760,520,3),(90,760,5),(910,740,4),(220,1000,3),(820,1020,5)])
b=stars+tx(500,180,'Jesus is the light',98,'#fbeec8')+tx(500,280,'a flashlight activity for Primary',58,'#f1b9a0','Cv',w=700)
b+=T(330,790,beam+flash,-14)
b+=tx(500,1170,'dim the lights',56,'#fbeec8','Fr')+tx(500,1250,'pass the flashlight',56,'#fbeec8','Fr')+tx(500,1330,'find the word light together',56,'#fbeec8','Fr')+tx(500,1410,'Psalm 27:1',46,'#f1b9a0','Cv',w=700)
PINS['act-light']=page(NAVY,b)
# 5 come
bush=''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,rx,ry,c,r in [(-190,40,120,70,'#8aa88e',-20),(-60,-10,130,80,'#a9c1a7',10),(80,30,140,80,'#8aa88e',-8),(200,-10,110,70,'#a9c1a7',16),(10,80,170,70,'#7a9a80',0),(-120,90,100,50,'#a9c1a7',6),(150,95,100,50,'#7a9a80',-6)])
pic=f'<g transform="rotate(8)"><rect x="-130" y="-105" width="260" height="210" rx="14" fill="#fffdf9" filter="url(#sh)"/><rect x="-106" y="-81" width="212" height="162" rx="6" fill="#f7e2a4"/><path d="M-106 81 q70 -90 140 -24 q36 -26 72 24z" fill="{SAGE}"/><circle cx="-36" cy="-20" r="28" fill="{MUST}"/><path d="M46 -8 c-34 -26 -22 -56 0 -44 c22 -12 34 20 0 44z" fill="{TERRA}"/></g>'
mag=f'<g transform="translate(0 0) rotate(-35)"><circle r="82" fill="#e9f3f8" fill-opacity=".55" stroke="{INK}" stroke-width="12"/><path d="M0 82 V190" stroke="{INK}" stroke-width="20" stroke-linecap="round"/><path d="M-44 -40 a56 56 0 0 1 36 -26" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round"/></g>'
b=tx(500,170,'A hide-and-find game',88,INK)+tx(500,262,'from John 1',88,INK)+tx(500,420,'&#8220;come and see!&#8221;',110,TERRA,'Cv',w=700)
b+=T(500,760,pic,0,1.25)+T(500,980,bush,0,1.2)+T(760,1130,mag,0,1.15)
b+=tx(500,1360,'hide a picture. let the kids go searching.',54,INK,'Cv',w=700)
PINS['act-come']=page('#e7efe2',b+foot())
# 6 plan
cloud=f'<path d="M-90 40 a46 46 0 0 1 10 -90 a60 60 0 0 1 112 -16 a48 48 0 0 1 72 70 a34 34 0 0 1 -10 36z" fill="#fff"/><path d="M-20 -20 l5 12 13 1-10 9 3 13-11-7-11 7 3-13-10-9 13-1z" fill="{MUST}" transform="translate(60 -10) scale(1.2)"/>'
earth=f'<circle r="100" fill="{BLUE}"/><path d="M-70 -50 q40 -30 66 0 q8 40 -30 48 q-30 -10 -36 -48z M18 20 q44 -8 60 30 q-18 40 -58 22z" fill="{SAGE}"/>'
house=f'<path d="M-100 20 L0 -80 L100 20z" fill="{TERRA}"/><rect x="-72" y="20" width="144" height="100" rx="8" fill="#fff"/><rect x="-20" y="58" width="40" height="62" rx="20" fill="{BROWN}"/><path d="M0 -8 c-24 -18 -14 -38 0 -28 c14 -10 24 10 0 28z" fill="#fff"/>'
b=tx(500,170,'Walk Heavenly',96,INK)+tx(500,275,'Father&#8217;s plan',96,INK)+tx(500,350,'a floor path game for Primary',56,TERRA,'Cv',w=700)
b+=f'<path d="M300 620 C 300 740 720 710 720 870 C 720 1000 300 970 300 1130 C 300 1230 700 1210 700 1280" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="2 20" stroke-linecap="round" opacity=".4"/>'
for (x,y,f_,a,n,l,lx,an) in [(300,620,'#dbe6f3',cloud,'1','before earth',470,'start'),(720,880,'#dfeadb',earth,'2','life on earth',560,'end'),(300,1150,BLUSH,house,'3','home again',470,'start')]:
    b+=medal(x,y,f_,a,n,l,lx,an)
PINS['act-plan']=page(CREAM,b+foot())
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(); pg=await br.new_page(viewport={'width':1000,'height':1500})
        for n,h in PINS.items():
            open(f'fun/m-{n}.html','w').write('<meta charset=utf-8>'+h); await pg.goto(f'file:///tmp/pins/fun/m-{n}.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(600)
            await pg.screenshot(path=f'fun/m-{n}.jpg',type='jpeg',quality=92)
        await br.close()
asyncio.run(main())
