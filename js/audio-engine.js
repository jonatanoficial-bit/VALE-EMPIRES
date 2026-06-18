(function(){
'use strict';
const MUSIC={
  menu:'assets/audio/music/menu-royal.ogg',
  exploration:'assets/audio/music/exploration-fields.ogg',
  combat:'assets/audio/music/combat-siege.ogg',
  victory:'assets/audio/music/victory-fanfare.ogg',
  defeat:'assets/audio/music/defeat-lament.ogg'
};
const SFX={
  'ui-click':'assets/audio/sfx/ui-click.ogg','ui-confirm':'assets/audio/sfx/ui-confirm.ogg','ui-error':'assets/audio/sfx/ui-error.ogg',
  'unit-select':'assets/audio/sfx/unit-select.ogg','command-move':'assets/audio/sfx/command-move.ogg','gather-wood':'assets/audio/sfx/gather-wood.ogg',
  'gather-food':'assets/audio/sfx/gather-food.ogg','gather-gold':'assets/audio/sfx/gather-gold.ogg','gather-stone':'assets/audio/sfx/gather-stone.ogg',
  construction:'assets/audio/sfx/construction.ogg',repair:'assets/audio/sfx/repair.ogg','sword-hit':'assets/audio/sfx/sword-hit.ogg',
  'arrow-shot':'assets/audio/sfx/arrow-shot.ogg','cavalry-charge':'assets/audio/sfx/cavalry-charge.ogg',impact:'assets/audio/sfx/impact.ogg',
  'unit-death':'assets/audio/sfx/unit-death.ogg','building-complete':'assets/audio/sfx/building-complete.ogg','era-complete':'assets/audio/sfx/era-complete.ogg',
  'tech-complete':'assets/audio/sfx/tech-complete.ogg','territory-capture':'assets/audio/sfx/territory-capture.ogg',autosave:'assets/audio/sfx/autosave.ogg',notification:'assets/audio/sfx/notification.ogg'
};
const STINGERS={england:'assets/audio/stingers/nation-england.ogg',france:'assets/audio/stingers/nation-france.ogg',byzantium:'assets/audio/stingers/nation-byzantium.ogg',mongol:'assets/audio/stingers/nation-mongol.ogg',cordoba:'assets/audio/stingers/nation-cordoba.ogg',norse:'assets/audio/stingers/nation-norse.ogg'};
const DEFAULTS={master:.85,music:.55,sfx:.78,ui:.68,muted:false,dynamic:true};
let prefs=loadPrefs();
let unlocked=false;
let pendingScene='menu';
let currentMusic=null,currentKey=null,ducked=false,combat=false,combatHoldTimer=null;
const lastPlayed=new Map();
const pools={};
function loadPrefs(){try{return {...DEFAULTS,...JSON.parse(localStorage.getItem('valeEmpires.audioPrefs')||'{}')}}catch{return {...DEFAULTS}}}
function persist(){localStorage.setItem('valeEmpires.audioPrefs',JSON.stringify(prefs));applyVolumes()}
function clamp(v){return Math.max(0,Math.min(1,Number(v)||0))}
function effectiveMusicVolume(){return prefs.muted?0:clamp(prefs.master*prefs.music*(ducked?.34:1))}
function effectiveSfxVolume(category='sfx'){return prefs.muted?0:clamp(prefs.master*(category==='ui'?prefs.ui:prefs.sfx))}
function ensureAudio(path,loop=false){const a=new Audio(path);a.preload='auto';a.loop=loop;a.playsInline=true;return a}
function preload(){Object.entries(SFX).forEach(([k,p])=>{const a=ensureAudio(p,false);a.volume=0;pools[k]=a});Object.values(MUSIC).forEach(p=>{const a=ensureAudio(p,true);a.volume=0});Object.values(STINGERS).forEach(p=>{const a=ensureAudio(p,false);a.volume=0})}
function unlock(){if(unlocked)return Promise.resolve(true);unlocked=true;const probe=ensureAudio(SFX['ui-click']);probe.volume=.001;return probe.play().then(()=>{probe.pause();probe.currentTime=0;applySceneMusic();return true}).catch(()=>{applySceneMusic();return false})}
function applyVolumes(){if(currentMusic)currentMusic.volume=effectiveMusicVolume()}
function fadeAudio(audio,from,to,duration=500,stopAtEnd=false){if(!audio)return;const start=performance.now();audio.volume=clamp(from);function step(now){const t=Math.min(1,(now-start)/duration);audio.volume=clamp(from+(to-from)*t);if(t<1)requestAnimationFrame(step);else if(stopAtEnd){audio.pause();audio.currentTime=0}}requestAnimationFrame(step)}
function playMusic(key,opts={}){if(!unlocked||prefs.muted)return;const path=MUSIC[key];if(!path)return;if(currentKey===key&&currentMusic&&!currentMusic.paused){applyVolumes();return}const old=currentMusic;const next=ensureAudio(path,opts.loop!==false);next.volume=0;next.play().then(()=>{currentMusic=next;currentKey=key;fadeAudio(next,0,effectiveMusicVolume(),opts.fade||650);if(old)fadeAudio(old,old.volume,0,opts.fade||650,true)}).catch(()=>{})}
function sceneTrack(scene){if(scene==='game')return combat&&prefs.dynamic?'combat':'exploration';if(scene==='campaign'||scene==='profile'||scene==='menu'||scene==='loading')return'menu';return'menu'}
function setScene(scene){pendingScene=scene;playMusic(sceneTrack(scene))}
function applySceneMusic(){setScene(pendingScene)}
function setCombat(active){if(!prefs.dynamic){combat=false;return}if(active){if(combatHoldTimer){clearTimeout(combatHoldTimer);combatHoldTimer=null}if(!combat){combat=true;if(pendingScene==='game')playMusic('combat',{fade:450})}}else if(combat){if(combatHoldTimer)clearTimeout(combatHoldTimer);combatHoldTimer=setTimeout(()=>{combat=false;combatHoldTimer=null;if(pendingScene==='game')playMusic('exploration',{fade:900})},3500)}}
function playSfx(name,opts={}){if(!unlocked||prefs.muted)return null;const src=SFX[name]||opts.src;if(!src)return null;const now=performance.now(),minGap=opts.minGap??35,last=lastPlayed.get(name)||0;if(now-last<minGap)return null;lastPlayed.set(name,now);const a=ensureAudio(src,false);a.volume=clamp(effectiveSfxVolume(opts.category||'sfx')*(opts.volume??1));a.playbackRate=Math.max(.65,Math.min(1.5,opts.rate||1));a.play().catch(()=>{});return a}
function playNationStinger(id){if(!unlocked||prefs.muted||!STINGERS[id])return;const a=ensureAudio(STINGERS[id],false);a.volume=clamp(effectiveSfxVolume('ui')*.9);duck(true);a.play().catch(()=>{});a.addEventListener('ended',()=>duck(false),{once:true})}
function playResult(victory){const key=victory?'victory':'defeat';if(!unlocked)return;const resume=sceneTrack(pendingScene);const old=currentMusic;if(old)fadeAudio(old,old.volume,0,350,true);const a=ensureAudio(MUSIC[key],false);a.volume=0;a.play().then(()=>{currentMusic=a;currentKey=key;fadeAudio(a,0,effectiveMusicVolume(),350);a.addEventListener('ended',()=>{currentMusic=null;currentKey=null;playMusic(resume,{fade:800})},{once:true})}).catch(()=>{})}
function duck(on=true){ducked=!!on;applyVolumes()}
function setPref(key,value){if(!(key in DEFAULTS))return;prefs[key]=typeof DEFAULTS[key]==='boolean'?!!value:clamp(value);persist();if(key==='dynamic'&&!prefs.dynamic&&combat){combat=false;if(pendingScene==='game')playMusic('exploration')}if(key==='muted'){if(prefs.muted){if(currentMusic)currentMusic.volume=0}else applySceneMusic()}}
function settingsHTML(){return `<div class="setting-card audio-settings-card"><h3>Áudio e música</h3><p>Trilha dinâmica e efeitos originais integrados nesta build.</p><div class="audio-setting-grid">
<label><span>Volume geral <b id="audioMasterLabel">${Math.round(prefs.master*100)}%</b></span><input id="audioMaster" type="range" min="0" max="100" value="${Math.round(prefs.master*100)}"></label>
<label><span>Música <b id="audioMusicLabel">${Math.round(prefs.music*100)}%</b></span><input id="audioMusic" type="range" min="0" max="100" value="${Math.round(prefs.music*100)}"></label>
<label><span>Efeitos <b id="audioSfxLabel">${Math.round(prefs.sfx*100)}%</b></span><input id="audioSfx" type="range" min="0" max="100" value="${Math.round(prefs.sfx*100)}"></label>
<label><span>Interface <b id="audioUiLabel">${Math.round(prefs.ui*100)}%</b></span><input id="audioUi" type="range" min="0" max="100" value="${Math.round(prefs.ui*100)}"></label>
</div><div class="audio-toggle-row"><label><input id="audioMuted" class="toggle" type="checkbox" ${prefs.muted?'checked':''}><span>Silenciar tudo</span></label><label><input id="audioDynamic" class="toggle" type="checkbox" ${prefs.dynamic?'checked':''}><span>Música dinâmica</span></label></div><div class="settings-action-row"><button class="hud-button" id="audioTestMusic">Testar música</button><button class="hud-button" id="audioTestSfx">Testar efeitos</button></div></div>`}
function bindSettings(){const pairs=[['audioMaster','master'],['audioMusic','music'],['audioSfx','sfx'],['audioUi','ui']];pairs.forEach(([id,key])=>{const el=document.getElementById(id),label=document.getElementById(id+'Label');if(!el)return;el.oninput=()=>{setPref(key,Number(el.value)/100);if(label)label.textContent=el.value+'%'}});const muted=document.getElementById('audioMuted');if(muted)muted.onchange=()=>setPref('muted',muted.checked);const dynamic=document.getElementById('audioDynamic');if(dynamic)dynamic.onchange=()=>setPref('dynamic',dynamic.checked);const music=document.getElementById('audioTestMusic');if(music)music.onclick=()=>{unlock();playMusic('menu',{fade:250})};const sfx=document.getElementById('audioTestSfx');if(sfx)sfx.onclick=()=>{unlock();playSfx('ui-confirm',{category:'ui',volume:1,minGap:0})}}
function diagnostics(){return{unlocked,pendingScene,currentKey,combat,ducked,prefs:{...prefs},musicCount:Object.keys(MUSIC).length,sfxCount:Object.keys(SFX).length,stingerCount:Object.keys(STINGERS).length}}
preload();
const unlockHandler=()=>unlock();document.addEventListener('pointerdown',unlockHandler,{once:true,capture:true});document.addEventListener('touchend',unlockHandler,{once:true,capture:true});
document.addEventListener('click',e=>{const b=e.target.closest('button');if(!b||b.disabled)return;unlock();if(!b.id?.startsWith('audioTest'))playSfx('ui-click',{category:'ui',volume:.72,minGap:45})},true);
document.addEventListener('visibilitychange',()=>{if(document.hidden){if(currentMusic)currentMusic.pause()}else if(unlocked){if(currentMusic)currentMusic.play().catch(()=>{});else applySceneMusic()}});
window.VALE_AUDIO={unlock,setScene,setCombat,playMusic,playSfx,playNationStinger,playResult,duck,setPref,getPrefs:()=>({...prefs}),settingsHTML,bindSettings,diagnostics,manifest:{MUSIC,SFX,STINGERS}};
})();
