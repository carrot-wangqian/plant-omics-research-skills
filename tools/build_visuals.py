#!/usr/bin/env python3
"""Build the release visual system from editable Python specifications and vector primitives."""
from __future__ import annotations
import concurrent.futures, html, math, os, random, shutil, subprocess
from pathlib import Path
from PIL import ImageFont
from visual_specs import DATA

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'/'release'
P='#f8f6ef'; W='#f2eee3'; ICE='#e7eff0'; MIST='#ebeee6'; LINE='#cad5d5'
INK='#14262a'; MUTED='#5a6b6e'; BLUE='#215c75'; DEEP='#173646'; ROUTE='#117964'; RED='#a64239'; BLUSH='#f3e3de'
DARK='#112d35'; DARK2='#173c43'; SPLASH='#72e2d4'; SOFT='#a7c7c7'; LIGHT='#e5f4ed'
FONTS={'serif':'"DejaVu Serif", Georgia, "Times New Roman", serif','sans':'"DejaVu Sans", Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif','mono':'"DejaVu Sans Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace'}
ORDER=['spatial-omics-paper-reading','plant-omics-preflight','plant-spatial-omics-analysis','analysis-explainer','scientific-figure-standard','plant-omics-thesis-writing']
E=lambda value:html.escape(str(value),quote=True)
FONTDIR=Path('/usr/share/fonts/truetype/dejavu')
def measure(s,n,f='sans',bold=False):
 name={'sans':'DejaVuSans','mono':'DejaVuSansMono','serif':'DejaVuSerif'}[f]+('-Bold' if bold else '')+'.ttf'
 try:return ImageFont.truetype(str(FONTDIR/name),n).getlength(s)
 except OSError:return len(s)*n*.59
def txt(x,y,s,size=34,f='sans',col=INK,w=400,a='start',ls=0):
 return f'<text x="{x}" y="{y}" font-family="{E(FONTS[f])}" font-size="{size}" font-weight="{w}" fill="{col}" text-anchor="{a}" letter-spacing="{ls}">{E(s)}</text>'
def fit(s,n,width,f='sans',bold=False):
 if measure(s,n,f,bold)>width:raise ValueError(f'Text too wide at {n}px, {width}px box: {s}')
 return s
def wrap(s,width,n,f='sans',bold=False):
 out=[]
 for paragraph in s.split('\n'):
  line=''
  for word in paragraph.split():
   candidate=' '.join(z for z in (line,word) if z)
   if line and measure(candidate,n,f,bold)>width:out.append(line);line=word
   else:line=candidate
  out.append(line)
 return out
def block(x,y,s,width,n=34,lead=None,f='sans',col=INK,w=400,a='start',limit=None):
 lines=wrap(s,width,n,f,w>=600);lead=lead or round(n*1.28)
 if limit is not None and len(lines)>limit:raise ValueError(f'Need at most {limit} lines: {s} gets {lines}')
 return ''.join(txt(x,y+i*lead,z,n,f,col,w,a) for i,z in enumerate(lines))
def rect(x,y,w,h,c=P,stroke='none',r=0,sw=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}" stroke="{stroke}" stroke-width="{sw}"/>'
def path(d,c=LINE,w=2,fill='none',dash=''):return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def circ(x,y,r,c=P,s=BLUE,sw=2):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{s}" stroke-width="{sw}"/>'
def label(x,y,s,c=BLUE,n=23):return txt(x,y,s,n,'mono',c,700,ls=2)
def svg(w,h,title,desc,inside,dark=False):
 bg=DARK if dark else P
 return '<?xml version="1.0" encoding="UTF-8"?>\n'+f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="visual-title visual-description"><title id="visual-title">{E(title)}</title><desc id="visual-description">{E(desc)}</desc>'+rect(0,0,w,h,bg)+("" if dark else rect(.5,.5,w-1,h-1,'none',LINE))+inside+"</svg>\n"
def rail(x1,y1,x2,y2,c=ROUTE,dash=''):
 angle=math.atan2(y2-y1,x2-x1); pts=[(x2,y2),(x2-14*math.cos(angle-.48),y2-14*math.sin(angle-.48)),(x2-14*math.cos(angle+.48),y2-14*math.sin(angle+.48))]
 return path(f'M{x1} {y1}L{x2} {y2}',c,4,dash=dash)+f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in pts)}" fill="{c}"/>'
def leaf(cx,cy,scale=1,dark=True):
 # Parametric outline, branching venation and independently paced assay dots.
 a=SPLASH if dark else BLUE;b=SOFT if dark else LINE
 base=f'<g transform="translate({cx} {cy}) scale({scale})">'
 base+=path('M38 441 C26 321 126 93 458 29 C447 142 426 281 309 397 C213 489 132 481 38 441Z',a,4,DARK2 if dark else ICE)
 base+=path('M4 466 C105 396 220 268 458 29',a,4)
 for i in range(1,11):
  t=i/11; x=39+394*t; y=439-393*t; reach=math.sin(math.pi*t)
  left=(x-126*reach,y-100*reach);right=(x+146*reach,y+86*reach)
  base+=path(f'M{x:.1f} {y:.1f}Q{x-55*reach:.1f} {y-23*reach:.1f} {left[0]:.1f} {left[1]:.1f}',b,2.2)
  base+=path(f'M{x:.1f} {y:.1f}Q{x+42*reach:.1f} {y+71*reach:.1f} {right[0]:.1f} {right[1]:.1f}',b,2.2)
  for k in (0.42,.69,.84):
   xx=x+(left[0]-x)*k;yy=y+(left[1]-y)*k
   base+=path(f'M{xx:.1f} {yy:.1f}l5 -17',a,1.3)
   xx=x+(right[0]-x)*k;yy=y+(right[1]-y)*k
   base+=path(f'M{xx:.1f} {yy:.1f}l19 -1',a,1.3)
 rng=random.Random(42)
 for iy in range(9):
  for ix in range(11):
   x=255+ix*19;y=282+iy*19
   if (ix-5)**2/36+(iy-3)**2/18>1.18 or rng.random()<.20:continue
   base+=circ(x,y,1.7+rng.random()*2.3,LIGHT if dark else BLUE,'none')
 return base+'</g>'
def card_inner(d,num):
 o=label(68,96,'PLANT OMICS RESEARCH SKILLS',BLUE,26)+txt(1012,96,f'{num:02d} / 06',28,'mono',MUTED,700,'end')
 o+=path('M68 130H1012')
 title=d['title']; n=80
 for i,s in enumerate(title):o+=txt(68,244+i*92,fit(s,n,950,'serif'),n,'serif')
 ypos=244+(len(title)-1)*92+72
 o+=block(70,ypos,d['promise'],940,35,43,col=MUTED,limit=2)
 y=550 if len(title)==2 else 609
 o+=rect(68,y,944,342 if len(title)==2 else 279,W,LINE,3)
 o+=path(f'M104 {y+45}h40m-20 -20v40 M936 {y+45}h40m-20 -20v40 M104 {y+235}h40m-20 -20v40 M936 {y+235}h40m-20 -20v40',LINE,1.4)
 s=1.16 if len(title)==2 else .97
 o+=f'<g transform="translate({540-170*s:.2f} {y+((342 if len(title)==2 else 279)-260*s)/2:.2f}) scale({s})">{d["icon"]}</g>'
 o+=rect(68,929,944,85,DEEP)
 o+=txt(95,982,fit(d['gate'],33,900,'sans',True),33,'sans',LIGHT,700)
 return o
def header(kicker,title,sub,w=1400):
 return label(57,61,kicker,n=23)+txt(55,133,fit(title,62,w-110,'serif'),62,'serif')+txt(57,184,fit(sub,29,w-112),29,'sans',MUTED)+path(f'M56 218H{w-56}',LINE,2)
def stopline(y,labeltext,detail):
 return rect(56,y,1288,85,BLUSH,'none',8)+label(83,y+35,labeltext,RED,23)+txt(83,y+66,fit(detail,28,1230),28,'sans',INK)
def generic_workflow(d,n):
 isread=n==1
 o=header(f'WORKFLOW / {n:02d}',d.get('workflow_title',' '.join(d['title'])),d['workflow_subtitle'])
 cols=(116,537,1005)
 if isread:
  for j,(h,t,b,c) in enumerate([('FULL TEXT','Use linked evidence.',ICE,BLUE),('PARTIAL','Use visible evidence; flag gaps.',MIST,ROUTE),('NO USABLE SOURCE','Request a source; STOP.',BLUSH,RED)]):
   x=56+j*435
   o+=rect(x,234,418,88,b,LINE,6)+label(x+17,266,h,c,21)
   if j==2:
    prefix=t.removesuffix('STOP.')
    o+=txt(x+17,299,fit(t,24,385),24).replace(E(t)+'</text>',E(prefix)+f'<tspan fill="{RED}" font-weight="700">STOP.</tspan></text>')
   else:o+=txt(x+17,299,fit(t,24,385),24)
 ly=357 if isread else 269
 o+=label(cols[0],ly,'STAGE')+label(cols[1],ly,'CHECK')+label(cols[2],ly,'RECORD')
 count=len(d['stages']);st_top=378 if isread else 292
 row=75 if isread else (91 if count==5 else 108)
 o+=path(f'M85 {st_top+37}V{st_top+(count-1)*row+37}',ROUTE,4)
 for i,(s,c,r) in enumerate(d['stages']):
  y=st_top+i*row
  o+=rect(107,y,1237,row-5,ICE if i%2==0 else W,LINE,4)
  o+=circ(85,y+37,20,P,ROUTE,4)+txt(85,y+44,str(i+1),19,'mono',DEEP,700,'middle')
  for x,t,w,fs,col in [(cols[0],s,402,40,INK),(cols[1],c,435,31,MUTED),(cols[2],r,317,29,BLUE)]:
   ls=wrap(t,w,fs,'sans',x==cols[0]); yy=y+(row-4-(len(ls)-1)*34)/2+10
   o+=block(x,yy,t,w,fs,34,col=col,w=700 if x==cols[0] else 400,limit=2)
 if isread:
  o+=path('M57 808H1343')+txt(58,851,'Optional handoff: preserve open questions and next steps.',29,'sans',MUTED)
 else:
  foot='Technical pass is not scientific approval.' if n==5 else d.get('workflow_footer',d['gate'])
  y=799
  if n==4:o+=stopline(y,'STOP', 'No rerun. No redraw. Explain the stored evidence.')
  else:o+=rect(56,y,1288,68,MIST,LINE,6)+txt(78,y+43,fit(foot,31,1235),31,'sans',DEEP,700)
 return o
def node(x,y,w,h,code,title,sub='',bg=ICE,accent=BLUE,fs=32):
 o=rect(x,y,w,h,bg,LINE,7)+label(x+15,y+27,code,accent,18)
 o+=block(x+15,y+61,title,w-30,fs,35,w=700,limit=3)
 if sub:o+=block(x+15,y+h-16,sub,w-30,22,25,col=MUTED,limit=1)
 return o
def preflight(d):
 o=header('WORKFLOW / 02','Plant Omics Preflight','Decide what is ready before analysis begins.')
 y=288
 for j,(code,t,sub) in enumerate([('01','Choose mode','Targeted by default'),('02','Bind inputs','Resolve files and IDs'),('03','Check\nprerequisites','Use modality checks'),('04','Set readiness','Record the decision')]):
  x=56+j*328;o+=node(x,y,304,143,code,t,sub,fs=35)
  if j<3:o+=rail(x+305,y+75,x+325,y+75)
 o+=label(56,265,'MODES: SCOPE REVIEW / TARGETED / INVENTORY',BLUE,19)
 o+=path('M1194 434V485H209 M209 485V526M538 485V526M867 485V526M1194 485V526',ROUTE,3)
 for j,(h,s,b,c) in enumerate([('Ready','Inputs meet checks',ICE,BLUE),('Conditional','Limits apply',MIST,ROUTE),('Blocked','Prerequisite missing',BLUSH,RED),('Not Applicable','',W,MUTED)]):
  x=56+j*328;o+=node(x,528,304,126,'STATE',h,s,b,c,37)
 o+=txt(57,720,'Document the scope, what was checked, and what remains open.',29,'sans',MUTED)
 return o+stopline(781,'HARD STOP','Preflight does not authorize execution.')
def analysis(d):
 o=header('WORKFLOW / 03','Plant Spatial Omics Analysis','Choose scope and modality, then document the decision.')
 o+=node(56,312,247,155,'01','Define comparison','Fix the unit',fs=29)
 o+=node(327,312,233,155,'02','Verify baseline','Check inputs',fs=29)
 o+=rail(304,391,324,391)
 o+=path('M561 391H590V332H613 M590 391V492H613',ROUTE,4)
 o+=node(615,270,314,127,'MODALITY A','MSI branch','Candidate evidence',ICE,BLUE,31)
 o+=node(615,435,314,127,'MODALITY B','scRNA / Spatial RNA','Cross-modality option',MIST,ROUTE,25)
 o+=path('M930 332H961V390H985M930 493H961V390',ROUTE,4)
 o+=node(990,312,354,155,'03 / AUTHORIZATION GATE','Compare options','Plan or run',ICE,BLUE,31)
 o+=path('M1172 467V592H186M1172 592V621M186 592V621',ROUTE,4)
 o+=node(56,623,275,131,'AUTHORIZED','Run in scope','Bounded comparison',ICE,BLUE,27)
 o+=node(352,623,279,131,'04','Audit retention','Missing is not zero',MIST,ROUTE,28)
 o+=rail(332,690,349,690)+rail(632,690,651,690)
 o+=node(654,623,304,131,'05','Record decision','Keep denominators',ICE,BLUE,28)
 o+=node(984,623,360,131,'NOT AUTHORIZED','Stop at the plan','Do not run',BLUSH,RED,30)
 o+=rect(56,796,1288,63,W,LINE,6)+txt(77,838,'Mass match is not compound confirmation; spots are not biological replicates.',27,'sans',DEEP,700)
 return o
def report(d,n):
 o=label(59,70,f'REPORT PREVIEW / {n:02d}',BLUE,23)
 o+=rect(59,98,1082,56,DEEP)
 o+=txt(78,135,'SYNTHETIC EXAMPLE · NOT REAL DATA',25,'mono',LIGHT,700,ls=1)
 ss=wrap(d['preview_title'],1060,54,'serif')
 if len(ss)>2:raise ValueError('Preview title too long')
 for j,t in enumerate(ss):o+=txt(57,222+j*58,t,54,'serif')
 y=263+58*(len(ss)-1); o+=label(60,y,d['preview_id'],MUTED,20)
 rows=d['preview']; heights=[]
 for k,v in rows:
  hh=max(len(wrap(v,818,29) if k=='Source lock' and n==5 else wrap(v,776,30)),len(wrap(k,213,28,'sans',True)))
  heights.append(max(72,hh*34+12))
 y+=30
 if y+sum(heights)>723:raise ValueError(f'Preview overset: {d["preview_title"]}')
 for (key,val),h in zip(rows,heights):
  o+=rect(59,y,1082,h-3,ICE if (rows.index((key,val))%2==0) else W,LINE,4)
  o+=block(76,y+40,key,213,28,33,col=BLUE,w=700,limit=2)
  o+=block(298,y+39,val,818,29 if key=='Source lock' and n==5 else 30,35,col=INK,limit=3)
  y+=h
 o+=path('M59 742H1141',LINE,2)+block(59,786,d['boundary'],1082,27,30,col=DEEP,w=700,limit=2)
 return o
def architecture():
 o=header('SUITE MAP / 06 INDEPENDENT SKILLS','How the six Skills work together','Enter at any point. The main route is a guide, not a requirement.',1600)
 o+=node(58,264,449,140,'01 / OPTIONAL INPUT','Spatial Omics Paper Reading','Published method ≠ project plan',MIST,ROUTE,28)
 o+=path('M507 336H1402 M532 336V408H495V439 M1402 336V439',ROUTE,4,dash='8 10')
 o+=label(544,316,'METHOD BENCHMARK',ROUTE,20)+label(1047,316,'CITATION & EVIDENCE',ROUTE,20)
 o+=rail(495,437,495,467,ROUTE,dash='6 7')+rail(1402,437,1402,467,ROUTE,dash='6 7')
 stages=[
 ('02','Plant Omics\nPreflight','File exists ≠ verified.\nReady ≠ authorized.'),
 ('03','Plant Spatial\nOmics Analysis','Mass match ≠ identity.'),
 ('04','Analysis\nExplainer','No test → no “significant.”\nNo rerun.'),
 ('05','Scientific\nFigure\nStandard','Technical pass ≠\nscientific approval.'),
 ('06','Plant Omics\nThesis Writing','Separate evidence,\nauthor decisions & literature.')]
 for i,(code,title,g) in enumerate(stages):
  x=57+300*i
  o+=node(x,470,276,159,code,title,fs=33)
  if i<4:o+=rail(x+276,536,x+297,536)
  o+=block(x+8,666,g,260,23,29,col=DEEP,w=600,limit=4)
  if code=='03':o+=txt(x+8,724,fit('Spots ≠ bio replicates.',20,260,bold=True),20,'sans',DEEP,600)
 o+=path('M495 744V763H265.5V775 M495 763H505.5V775',BLUE,3)
 o+=rect(126,779,279,52,W,LINE,5)+label(149,811,'AUTHORIZATION GATE',BLUE,19)
 o+=rect(417,779,177,52,MIST,LINE,5)+label(438,811,'MSI BRANCH',ROUTE,19)
 o+=txt(746,811,'Guardrails stay attached to each decision.',27,'sans',MUTED)
 return o
def hero():
 o=rect(0,0,1280,640,DARK)
 for j in range(8):o+=path(f'M738 {55+j*76}H1225',DARK2,1.4)
 for j in range(7):o+=path(f'M{748+j*79} 44V605',DARK2,1.4)
 o+=path('M65 140H672 M65 512H672',SOFT,1)
 o+=label(65,93,'PLANT SPATIAL RESEARCH / 06',SPLASH,22)
 o+=txt(61,235,'Plant Omics',87,'serif',LIGHT,700)+txt(62,336,'Research Skills',79,'serif',LIGHT,700)
 o+=block(66,406,'6 independent, evidence-linked skills for plant spatial & single-cell omics',667,32,43,col=SOFT,limit=2)
 o+=label(67,565,'VERIFY SOURCE  /  BOUND CLAIMS',SPLASH,19)
 o+=leaf(737,57,.95,True)
 o+=label(782,576,'TISSUE × SPATIAL SIGNAL',SPLASH,18)
 return o
def cards_grid():
 o=''
 for idx,key in enumerate(ORDER):
  x=21+(idx%3)*550;y=19+(idx//3)*552
  d=DATA[key]
  o+=f'<g transform="translate({x} {y}) scale(0.498)">'+rect(0,0,1080,1080,P,LINE,6,2)+card_inner(d,idx+1)+'</g>'
 return o
def mmd_suite():
 return """flowchart LR
 R["01 Spatial Omics Paper Reading"] -. "Method benchmark" .-> A
 R -. "Citation and evidence" .-> W
 P["02 Plant Omics Preflight"] --> A["03 Plant Spatial Omics Analysis"]
 A --> E["04 Analysis Explainer"] --> F["05 Scientific Figure Standard"] --> W["06 Plant Omics Thesis Writing"]
 A --- G["Authorization Gate"]
 A --- M["MSI branch"]
"""
def write(out,rendered):
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(rendered,encoding='utf-8')
 return out
def main():
 if not shutil.which('inkscape'):raise SystemExit('Inkscape CLI is required to export high-resolution PNGs.')
 jobs=[]
 jobs.append(write(OUT/'hero-banner.svg',svg(1280,640,'Plant Omics Research Skills','Six independent evidence-linked skills, illustrated by a leaf with venation and a spatial measurement grid.',hero(),True)))
 jobs.append(write(OUT/'suite-architecture.svg',svg(1600,900,'How the six Skills work together','Paper reading is an optional evidence input to analysis and writing. A five-node main route supports preflight, analysis, interpretation, plotting and writing; authorization and MSI are explicit analysis branches.',architecture())))
 jobs.append(write(OUT/'cards-overview.svg',svg(1680,1136,'The six Skill cards','A three by two gallery of distinct cards for paper reading, preflight, analysis, explanation, figure design, and thesis writing.',cards_grid())))
 write(OUT/'suite-architecture.mmd',mmd_suite())
 for i,key in enumerate(ORDER,1):
  d=DATA[key]; b=OUT/key; name=' '.join(d['title'])
  jobs.append(write(b/'card.svg',svg(1080,1080,name,d['promise']+' '+d['gate'],card_inner(d,i))))
  flow=preflight(d) if i==2 else analysis(d) if i==3 else generic_workflow(d,i)
  jobs.append(write(b/'workflow.svg',svg(1400,900,name+' workflow',d.get('workflow_desc','; '.join(' — '.join(x) for x in d['stages'])),flow)))
  jobs.append(write(b/'report-preview.svg',svg(1200,840,d['preview_title'],'Synthetic example, not real data. '+d['boundary'],report(d,i))))
  write(b/'workflow.mmd',d['mermaid'].strip()+'\n')
 def export(f):
  env=os.environ.copy(); env.setdefault('XDG_CACHE_HOME',str(Path('/tmp')/'plant-omics-visual-cache'))
  proc=subprocess.run(['inkscape',str(f),'--export-type=png','--export-filename='+str(f.with_suffix('.png')), '--export-dpi=96'],capture_output=True,text=True,env=env)
  if proc.returncode:raise RuntimeError(f'{f}: {proc.stderr}')
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(export,jobs))
 print(f'Built {len(jobs)} editable SVGs, {len(jobs)} PNGs, and 7 editable Mermaid files.')
if __name__=='__main__':main()
