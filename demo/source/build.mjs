import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const HERE=path.dirname(fileURLToPath(import.meta.url));
const REPO=path.resolve(HERE,'../..');
const AS=path.resolve(REPO,'demo/assets');
const OUT=path.resolve(REPO,'demo');
const PRE=path.resolve(HERE,'previews');
const C={bg:'#F0F0EE',paper:'#FAF9F5',ink:'#1F1E1C',meta:'#504F4B',muted:'#8F8E86',faint:'#C0BFB7',hero:'#F5572F'};
const W=1280,H=720;
await fs.mkdir(PRE,{recursive:true});

async function bytes(path){const b=await fs.readFile(path);return b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength)}
async function writeBlob(path,blob){await fs.writeFile(path,new Uint8Array(await blob.arrayBuffer()))}
function shape(slide,name,position,fill='none',line={style:'solid',fill:'none',width:0},geometry='rect'){
  return slide.shapes.add({geometry,name,position,fill,line});
}
function text(slide,name,content,position,style={}){
  const s=shape(slide,name,position,'none');
  s.text=content;
  s.text.style={fontFamily:'Arial',fontSize:24,color:C.ink,...style};
  return s;
}
function eyebrow(slide,content){return text(slide,'eyebrow',content.toUpperCase(),{left:72,top:56,width:570,height:24},{fontSize:12,bold:true,color:C.meta,characterSpacing:2})}
function page(slide,n){return text(slide,'page-number',`${String(n).padStart(2,'0')} / 08`,{left:1140,top:56,width:68,height:18},{fontSize:11,bold:true,color:C.meta,alignment:'right',characterSpacing:1})}
function pageOnImage(slide,n){shape(slide,'page-number-contrast-field',{left:1128,top:44,width:88,height:42},C.paper,{style:'solid',fill:'#D1D0CA',width:1});return text(slide,'page-number',`${String(n).padStart(2,'0')} / 08`,{left:1138,top:57,width:68,height:18},{fontSize:11,bold:true,color:C.ink,alignment:'right',characterSpacing:1})}
function notes(slide,sourceLines,cues){
  slide.speakerNotes.textFrame.setText(`[Sources]\n${sourceLines.join('\n')}\n\n[Animation cues — static PPTX fallback]\n${cues.join('\n')}\n\n[Motion status]\nObjects are independently selectable, but this PPTX intentionally contains no claimed native timing tree. Use the cues above or the companion HTML for verified motion.`);
  slide.speakerNotes.setVisible(true);
}
async function addImg(slide,name,path,position,alt,fit='cover'){
  const im=slide.images.add({name,blob:await bytes(path),contentType:'image/png',alt:`${name}: ${alt}`,fit,position});
  try{im.name=name}catch{}
  return im;
}
function label(slide,name,content,left,top,width){return text(slide,name,content,{left,top,width,height:22},{fontSize:11,bold:true,color:C.meta,characterSpacing:1})}

const deck=Presentation.create({slideSize:{width:W,height:H}});

// 01 — compact aperture / opening scene
{
  const s=deck.slides.add();s.background.fill=C.bg;
  await addImg(s,'s01-scene-a',`${AS}/cover-market.png`,{left:0,top:0,width:W,height:H},'Abstract paper market forms gather around a small orange opening.');
  shape(s,'s01-copy-field',{left:0,top:0,width:528,height:H},C.bg);
  text(s,'s01-eyebrow','A COMPLEX ZINE-ANCHOR DEMONSTRATION',{left:72,top:164,width:410,height:24},{fontSize:12,bold:true,color:C.muted,characterSpacing:2});
  text(s,'s01-title','Memory is\ninfrastructure',{left:72,top:214,width:550,height:138},{fontSize:58,bold:true,color:C.ink});
  text(s,'s01-subtitle','A market is remembered through patterns—not monuments.',{left:72,top:380,width:390,height:66},{fontSize:22,color:'#4F4E49'});
  shape(s,'s01-anchor-chip',{left:72,top:508,width:28,height:10},C.hero);
  text(s,'s01-deck-name','THE THRESHOLD AS A LIVING SYSTEM',{left:112,top:499,width:350,height:24},{fontSize:11,bold:true,color:C.ink,characterSpacing:1});
  pageOnImage(s,1);
  notes(s,['Original illustration generated with OpenAI image generation for this demonstration.','No external factual claims.'],['Reveal s01-scene-a through a left-to-right mask over 0.6 seconds.','Hold the orange aperture as the visual anchor state: compact opening.']);
}

// 02 — four-layer model / seam anchor
{
  const s=deck.slides.add();s.background.fill=C.bg;eyebrow(s,'A pattern has layers');page(s,2);
  text(s,'s02-title','Four layers make the pattern legible',{left:72,top:96,width:900,height:58},{fontSize:42,bold:true});
  const rows=[
    ['01','OBJECTS','Stalls, tarps, tools, signs','The visible kit of everyday trade.'],
    ['02','RITUALS','Opening, exchange, pause','Sequences that make use recognizable.'],
    ['03','ROUTES','Approach, passage, return','Movement that connects repeated encounters.'],
    ['04','ACCESS','Affordability, presence, choice','Conditions that keep participation possible.'],
  ];
  const ys=[205,310,415,520];
  for(let i=0;i<rows.length;i++){
    const [n,k,title,desc]=rows[i];
    shape(s,`s02-row-${n}-rule`,{left:72,top:ys[i],width:1136,height:1},C.faint);
    text(s,`s02-row-${n}-number`,n,{left:72,top:ys[i]+29,width:42,height:28},{fontSize:12,bold:true,color:C.meta,characterSpacing:1});
    text(s,`s02-row-${n}-kind`,k,{left:132,top:ys[i]+28,width:130,height:28},{fontSize:13,bold:true,color:C.ink,characterSpacing:1});
    shape(s,`s02-row-${n}-anchor`,{left:288,top:ys[i]+33,width:34,height:9},C.hero);
    text(s,`s02-row-${n}-title`,title,{left:354,top:ys[i]+20,width:390,height:44},{fontSize:26,bold:true});
    text(s,`s02-row-${n}-desc`,desc,{left:810,top:ys[i]+22,width:370,height:40},{fontSize:16,color:'#55544F'});
  }
  notes(s,['Concept model authored for this demonstration; no external factual claims.'],['Reveal the four row compartments from top to bottom with 0.12-second overlap.','The orange seam advances one row at a time; anchor state: reading seam.']);
}

// 03 — three independent ritual scenes
{
  const s=deck.slides.add();s.background.fill=C.bg;eyebrow(s,'Recognition lives in repetition');page(s,3);
  text(s,'s03-title','Three everyday rituals keep recognition alive',{left:72,top:94,width:980,height:60},{fontSize:42,bold:true});
  const xs=[72,440,824], tops=[220,194,220], widths=[320,300,360];
  const labels=['01 · STALL','02 · EXCHANGE','03 · PASSAGE'];
  const names=['s03-scene-a','s03-scene-b','s03-scene-c'];
  const files=['ritual-stall.png','ritual-exchange.png','ritual-passage.png'];
  const alts=['A simplified market stall beneath a torn canopy.','Two abstract hands exchange a small parcel.','A small figure moves along a narrow market passage.'];
  for(let i=0;i<3;i++){
    await addImg(s,names[i],`${AS}/${files[i]}`,{left:xs[i],top:tops[i],width:widths[i],height:382},alts[i],'contain');
    text(s,`${names[i]}-caption`,labels[i],{left:xs[i]+10,top:624,width:widths[i]-20,height:24},{fontSize:12,bold:true,characterSpacing:1});
  }
  notes(s,['Original three-part illustration generated with OpenAI image generation.','Each scene is a separate image object and remains independently selectable.'],['Animate s03-scene-a, then s03-scene-b, then s03-scene-c.','Entrance: rise 18 px and fade; duration 0.52 seconds each; 0.13-second overlap.','Reduced-motion equivalent: show all three in final position.']);
}

// 04 — constricted route / image compartment below title reserve
{
  const s=deck.slides.add();s.background.fill=C.bg;
  await addImg(s,'s04-scene-a',`${AS}/narrow-threshold.png`,{left:0,top:200,width:W,height:520},'Charcoal market fragments press around a narrow orange passage.');
  shape(s,'s04-title-field',{left:0,top:0,width:W,height:200},C.bg);
  eyebrow(s,'The tension is spatial');page(s,4);
  text(s,'s04-title','A narrowed route makes every other layer fragile',{left:72,top:92,width:985,height:66},{fontSize:42,bold:true});
  shape(s,'s04-note-contrast-field',{left:64,top:624,width:800,height:58},C.ink);
  text(s,'s04-note','A path can remain technically open—and still stop carrying the rituals people recognize.',{left:80,top:642,width:768,height:28},{fontSize:16,bold:true,color:C.paper});
  notes(s,['Original illustration generated with OpenAI image generation.','No external factual claims.'],['Reveal s04-scene-a with a horizontal clip expanding from the orange seam; 0.7 seconds.','Anchor state: constricted but not closed.']);
}

// 05 — Lieflat L14 Hundred Field
{
  const s=deck.slides.add();s.background.fill=C.bg;eyebrow(s,'Simulated demonstration data');page(s,5);
  text(s,'s05-title','Preserve the pattern\n64 to 23',{left:72,top:104,width:390,height:110},{fontSize:43,bold:true});
  text(s,'s05-metric','+41',{left:72,top:252,width:172,height:96},{fontSize:78,bold:true,color:C.hero});
  text(s,'s05-metric-unit','percentage points',{left:220,top:306,width:220,height:32},{fontSize:18,bold:true});
  text(s,'s05-explain','One mark equals one percentage point. The orange cluster turns the threshold into evidence.',{left:72,top:380,width:365,height:86},{fontSize:19,color:'#4F4E49'});
  text(s,'s05-footnote','Illustrative values only: preserve 64%, redevelop 23%, undecided 13%.',{left:72,top:522,width:365,height:48},{fontSize:11,color:'#686761'});
  shape(s,'s05-chart-frame',{left:500,top:112,width:708,height:505},C.paper,{style:'solid',fill:'#D4D3CC',width:1});
  label(s,'s05-chart-label','L14 · HUNDRED FIELD / WIRE',522,126,330);
  await addImg(s,'s05-scene-a-lieflat-chart',`${AS}/hundred-field.png`,{left:522,top:154,width:664,height:438},'One hundred marks show 64 for preservation, 23 for redevelopment, and 13 undecided.','contain');
  notes(s,['Simulated demonstration data: preserve 64%, redevelop 23%, undecided 13%; not a real survey.','Chart system: Lieflat Charts L14 Hundred Field, Wire color system. Lieflat Charts was created at Moxt and is distributed by larashero3-dotcom. PolyForm Noncommercial 1.0.0; this is a noncommercial demonstration.','Template audit: L14 selected; F4 Tick Donut rejected because comparison is slower; L5 radial convergence rejected because it adds relationship geometry absent from the data.'],['Reveal marks with the L14 phyllotaxis stagger; preservation cluster first.','Duration about 0.76 seconds; reduced-motion equivalent shows all marks immediately.','Companion HTML includes click-to-replay.']);
}

// 06 — Lieflat L15 Ballot Tally
{
  const s=deck.slides.add();s.background.fill=C.bg;eyebrow(s,'What should change protect?');page(s,6);
  text(s,'s06-title','Access priorities outrank maximum footprint',{left:72,top:94,width:955,height:64},{fontSize:42,bold:true});
  shape(s,'s06-chart-frame',{left:72,top:196,width:792,height:432},C.paper,{style:'solid',fill:'#D4D3CC',width:1});
  label(s,'s06-chart-label','L15 · BALLOT TALLY / WIRE',94,210,330);
  await addImg(s,'s06-scene-a-lieflat-chart',`${AS}/ballot-tally.png`,{left:94,top:244,width:748,height:352},'Four ballot rows: affordable stalls 72, vendor access 61, safer infrastructure 54, maximize footprint 22.','contain');
  text(s,'s06-callout','72',{left:920,top:260,width:172,height:92},{fontSize:76,bold:true,color:C.hero});
  text(s,'s06-callout-label','affordable stalls',{left:924,top:352,width:230,height:32},{fontSize:20,bold:true});
  text(s,'s06-note','The strongest request is not stasis. It is continued participation.',{left:924,top:422,width:270,height:92},{fontSize:18,color:'#4F4E49'});
  text(s,'s06-footnote','Illustrative tally only; values are simulated for this deck.',{left:924,top:552,width:270,height:42},{fontSize:11,color:'#686761'});
  notes(s,['Simulated demonstration values: affordable stalls 72, vendor access 61, safer infrastructure 54, maximize footprint 22; not a real ballot.','Chart system: Lieflat Charts L15 Ballot Tally, Wire color system. Lieflat Charts was created at Moxt and is distributed by larashero3-dotcom. PolyForm Noncommercial 1.0.0; this is a noncommercial demonstration.','Template audit: L15 selected for explicit vote counting; conventional bar chart rejected because tally accumulation is the story.'],['Reveal each ballot row left to right; 0.10-second stagger between rows.','The orange affordable-stalls row resolves last as the persistent visual anchor.','Companion HTML includes click-to-replay and reduced-motion support.']);
}

// 07 — three-part decision framework; anchor path stays below text
{
  const s=deck.slides.add();s.background.fill=C.bg;eyebrow(s,'A decision rule');page(s,7);
  text(s,'s07-title','Change is viable when it protects rhythm, access,\nand adaptation',{left:72,top:92,width:1015,height:108},{fontSize:42,bold:true});
  const cards=[
    {x:72,y:270,n:'01 / RHYTHM',h:'Protect repetition',p:'Retain the cues and sequences through which daily rituals remain recognizable.'},
    {x:500,y:340,n:'02 / ACCESS',h:'Keep participation\npossible',p:'Protect affordable stalls, vendor presence, and routes people can still use.'},
    {x:926,y:270,n:'03 / ADAPTATION',h:'Permit visible\nchange',p:'Upgrade safety and infrastructure without erasing the pattern that carries memory.'},
  ];
  for(let i=0;i<cards.length;i++){
    const c=cards[i];
    label(s,`s07-station-${i+1}-number`,c.n,c.x,c.y,280);
    text(s,`s07-station-${i+1}-title`,c.h,{left:c.x,top:c.y+36,width:290,height:72},{fontSize:29,bold:true});
    text(s,`s07-station-${i+1}-body`,c.p,{left:c.x,top:c.y+126,width:290,height:70},{fontSize:15,color:'#55544F'});
  }
  shape(s,'s07-anchor-path-a',{left:112,top:610,width:294,height:13},C.hero);
  shape(s,'s07-anchor-path-b',{left:402,top:605,width:270,height:18},C.hero);
  shape(s,'s07-anchor-path-c',{left:668,top:611,width:500,height:12},C.hero);
  notes(s,['Decision framework authored for this demonstration; no external factual claims.'],['Reveal the three station compartments in sequence: rhythm, access, adaptation.','Draw the orange anchor path only after all body text has settled; keep it below the text reserve.','Reduced-motion equivalent: show the complete rule and path at once.']);
}

// 08 — open passage / colophon
{
  const s=deck.slides.add();s.background.fill=C.bg;
  await addImg(s,'s08-scene-a',`${AS}/open-passage.png`,{left:0,top:202,width:W,height:518},'An open orange passage remains between calm charcoal market forms.');
  shape(s,'s08-title-field',{left:0,top:0,width:W,height:202},C.bg);
  eyebrow(s,'A closing proposition');page(s,8);
  text(s,'s08-title','Keep the threshold open enough for memory to move',{left:72,top:91,width:1015,height:70},{fontSize:43,bold:true});
  shape(s,'s08-credit-field',{left:72,top:624,width:1136,height:66},C.bg,{style:'solid',fill:'#9C9B95',width:1});
  text(s,'s08-credits-left','VISUAL SYSTEMS · Zine art direction: Zeejay0. Lieflat Charts: created at Moxt, distributed by larashero3-dotcom; L14 Hundred Field + L15 Ballot Tally, Wire; PolyForm Noncommercial 1.0.0.',{left:84,top:632,width:650,height:50},{fontSize:9.5,color:C.ink});
  text(s,'s08-credits-right','PRODUCTION · Original illustrations: OpenAI image generation. PPTX workflow: OpenAI Presentations. Simulated data, not a real survey. No external factual claims.',{left:758,top:632,width:430,height:50},{fontSize:9.5,color:C.ink});
  notes(s,['Zine visual direction: Zeejay0.','Lieflat Charts: created at Moxt, distributed by larashero3-dotcom; PolyForm Noncommercial 1.0.0.','OpenAI Presentations and OpenAI image generation used for production.'],['Soft reveal of s08-scene-a over 0.6 seconds.','Anchor state: the orange threshold opens into a stable passage.']);
}

for(const [i,s] of deck.slides.items.entries()){
  await writeBlob(`${PRE}/slide-${i+1}.png`,await deck.export({slide:s,format:'png',scale:1}));
  await fs.writeFile(`${PRE}/slide-${i+1}.layout.json`,await (await s.export({format:'layout'})).text());
}
await writeBlob(`${PRE}/deck-montage.webp`,await deck.export({format:'webp',montage:true,scale:1}));
try{
  await (await PresentationFile.exportPptx(deck)).save(`${OUT}/zine-anchor-complex-demo.pptx`);
}catch(error){
  console.error('EXPORT_FAIL',error?.message||String(error));
  if(error?.stack) console.error(error.stack.split('\n').slice(0,8).join('\n'));
  process.exitCode=1;
  throw new Error('PPTX export failed; see EXPORT_FAIL above.');
}
await fs.writeFile(`${PRE}/inspect.ndjson`,(await deck.inspect({kind:'slide,textbox,shape,image,notes,layout',maxChars:100000})).ndjson);
console.log(`Wrote ${OUT}/zine-anchor-complex-demo.pptx`);
