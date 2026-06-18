(function(){
'use strict';
const BUILD=window.VALE_BUILD||{};
const REQUIRED_IDS=['app','loadingScreen','menuScreen','periodScreen','profileScreen','skirmishScreen','campaignScreen','gameScreen','modalOverlay','recoveryOverlay','gameCanvas','minimapCanvas','btnNewGame','btnSkirmishMenu','btnContinue','btnSettings','btnCredits','btnLanguageMenu','languageOverlay','btnPeriodConfirm','btnDiplomacyPanel','btnCityAdminPanel','btnProvincePanel','btnRoyalCouncilPanel','btnCourtIntriguePanel','btnSecretOpsPanel','btnInfoWarfarePanel','btnCulturalMoralePanel','diplomacyOverlay','btnDiplomacyClose','btnRecoverRestart','btnRecoverSafe','btnRecoverBack'];
const CRITICAL_ASSETS=[
  'assets/branding/vale-empires-logo-fullscreen.png','assets/backgrounds/menu-main-background.png','assets/backgrounds/loading-screen-background.png',
  'assets/placeholders/test-placeholder-emblem.png','assets/terrain/terrain-grass-light.png','assets/terrain/terrain-water-shallow.png',
  'assets/factions/flags/reino-da-inglaterra-thumb.png','assets/factions/flags/reino-da-franca-thumb.png','assets/factions/flags/imperio-bizantino-thumb.png',
  'assets/factions/flags/imperio-mongol-thumb.png','assets/factions/flags/califado-de-cordoba-thumb.png','assets/factions/flags/reinos-nordicos-thumb.png'
];
const VALID_PACKS=new Set(['medieval','renaissance','industrial','early-1900s','modern']);
const ENABLED_PACKS=new Set(['medieval']);
const REPORT={generatedAt:new Date().toISOString(),build:{...BUILD},environment:{userAgent:navigator.userAgent,language:navigator.language,gameLocale:localStorage.getItem('valeEmpires.language')||'pt-BR',platform:navigator.platform,viewport:{width:innerWidth,height:innerHeight,dpr:devicePixelRatio||1},online:navigator.onLine,standalone:matchMedia?.('(display-mode: standalone)').matches||false,fullscreen:!!document.fullscreenElement},dom:{required:[...REQUIRED_IDS],missing:[]},assets:{checked:0,loaded:0,failed:[]},storage:{},errors:[],warnings:[],events:[]};
function addEvent(type,message,data=null){REPORT.events.push({at:new Date().toISOString(),type,message,data});}
function normalizePack(id){return VALID_PACKS.has(id)&&ENABLED_PACKS.has(id)?id:'medieval';}
function migrateSave(save){
  if(!save||typeof save!=='object')return save;
  const original=Number(save.schemaVersion||1),migrated={...save};
  migrated.buildId=migrated.buildId||BUILD.buildId||'unknown';
  migrated.eraPack=normalizePack(migrated.eraPack||migrated.profile?.eraPack||'medieval');
  migrated.profile=migrated.profile&&typeof migrated.profile==='object'?{...migrated.profile,eraPack:migrated.eraPack}:migrated.profile||null;
  if(!Array.isArray(migrated.buildings))migrated.buildings=[];
  if(!Array.isArray(migrated.units))migrated.units=[];
  if(!Array.isArray(migrated.enemies))migrated.enemies=[];
  if(!migrated.campaignProgress)migrated.campaignProgress={completed:[],unlocked:['foundation'],rewards:{}};
  if(!migrated.technologies)migrated.technologies=[];
  migrated.gameMode=migrated.gameMode==='skirmish'?'skirmish':'campaign';
  migrated.skirmish=migrated.gameMode==='skirmish'&&migrated.skirmish?migrated.skirmish:null;
  if(!migrated.diplomacy||typeof migrated.diplomacy!=='object')migrated.diplomacy=null;
  if(!migrated.tradeWorld||typeof migrated.tradeWorld!=='object')migrated.tradeWorld=null;
  if(!migrated.navalWorld||typeof migrated.navalWorld!=='object')migrated.navalWorld=null;
  if(!migrated.navalMilitary||typeof migrated.navalMilitary!=='object')migrated.navalMilitary=null;
  if(!migrated.coastalSiege||typeof migrated.coastalSiege!=='object')migrated.coastalSiege=null;
  if(!migrated.urbanSiege||typeof migrated.urbanSiege!=='object')migrated.urbanSiege=null;
  if(!migrated.cityAdministration||typeof migrated.cityAdministration!=='object')migrated.cityAdministration=null;
  if(!migrated.provinceNetwork||typeof migrated.provinceNetwork!=='object')migrated.provinceNetwork=null;
  if(!migrated.royalPolitics||typeof migrated.royalPolitics!=='object')migrated.royalPolitics=null;
  if(!migrated.courtIntrigue||typeof migrated.courtIntrigue!=='object')migrated.courtIntrigue=null;
  if(!migrated.secretOperations||typeof migrated.secretOperations!=='object')migrated.secretOperations=null;
  if(!migrated.informationWarfare||typeof migrated.informationWarfare!=='object')migrated.informationWarfare=null;
  if(!migrated.culturalMorale||typeof migrated.culturalMorale!=='object')migrated.culturalMorale=null;
  migrated.schemaVersion=19;
  if(original<19){migrated.migratedFrom=original;migrated.migratedAt=new Date().toISOString();addEvent('save-migration',`Save migrado do schema ${original} para 19`,{eraPack:migrated.eraPack,gameMode:migrated.gameMode});}
  return migrated;
}
function captureStorage(){for(const key of ['valeEmpires.save','valeEmpires.save.campaign','valeEmpires.save.skirmish','valeEmpires.save.backup','valeEmpires.save.campaign.backup','valeEmpires.save.skirmish.backup','valeEmpires.profile','valeEmpires.campaign','valeEmpires.eraPack','valeEmpires.audioPrefs','valeEmpires.lastSaveAt','valeEmpires.language','valeEmpires.skirmish','valeEmpires.secretOperations','valeEmpires.informationWarfare','valeEmpires.culturalMorale']){let raw=null;try{raw=localStorage.getItem(key)}catch(err){REPORT.warnings.push(`Storage indisponível: ${err.message}`)}REPORT.storage[key]={present:raw!==null,bytes:raw?new Blob([raw]).size:0,validJSON:true};if(raw&&!['valeEmpires.lastSaveAt','valeEmpires.language','valeEmpires.eraPack'].includes(key)){try{JSON.parse(raw)}catch{REPORT.storage[key].validJSON=false;REPORT.warnings.push(`JSON inválido em ${key}`)}}}}
function checkDOM(){REPORT.dom.missing=REQUIRED_IDS.filter(id=>!document.getElementById(id));if(REPORT.dom.missing.length)REPORT.errors.push(`IDs obrigatórios ausentes: ${REPORT.dom.missing.join(', ')}`);}
function checkAsset(src){return new Promise(resolve=>{const img=new Image();img.onload=()=>resolve({src,ok:true});img.onerror=()=>resolve({src,ok:false});img.src=src+(src.includes('?')?'&':'?')+'preflight='+encodeURIComponent(BUILD.version||'0');});}
async function checkAssets(){const result=await Promise.all(CRITICAL_ASSETS.map(checkAsset));REPORT.assets.checked=result.length;REPORT.assets.loaded=result.filter(x=>x.ok).length;REPORT.assets.failed=result.filter(x=>!x.ok).map(x=>x.src);if(REPORT.assets.failed.length)REPORT.warnings.push(`Assets críticos em fallback: ${REPORT.assets.failed.join(', ')}`);}
function downloadReport(){captureStorage();REPORT.generatedAt=new Date().toISOString();REPORT.environment.viewport={width:innerWidth,height:innerHeight,dpr:devicePixelRatio||1};REPORT.environment.online=navigator.onLine;REPORT.environment.fullscreen=!!document.fullscreenElement;REPORT.audio=window.VALE_AUDIO?.diagnostics?.()||null;const blob=new Blob([JSON.stringify(REPORT,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=`vale-empires-diagnostico-${BUILD.buildId||'build'}-${Date.now()}.json`;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},1000);}
function wireDiagnostics(){document.getElementById('btnDownloadDiagnostics')?.addEventListener('click',downloadReport);document.getElementById('diagnosticsSettingsBtn')?.addEventListener('click',downloadReport);}
window.addEventListener('error',e=>{REPORT.errors.push({type:'error',message:e.message,source:e.filename,line:e.lineno,column:e.colno,stack:e.error?.stack||null});addEvent('runtime-error',e.message);});
window.addEventListener('unhandledrejection',e=>{REPORT.errors.push({type:'unhandledrejection',message:String(e.reason?.message||e.reason),stack:e.reason?.stack||null});addEvent('promise-rejection',String(e.reason));});
window.addEventListener('online',()=>addEvent('connection','online'));window.addEventListener('offline',()=>addEvent('connection','offline'));
window.addEventListener('DOMContentLoaded',async()=>{checkDOM();captureStorage();wireDiagnostics();await checkAssets();addEvent('preflight','Concluído',{missingDOM:REPORT.dom.missing.length,failedAssets:REPORT.assets.failed.length});});
window.VALE_RELEASE_GUARD={report:REPORT,migrateSave,downloadReport,addEvent,runPreflight:async()=>{checkDOM();captureStorage();await checkAssets();return REPORT;}};
})();
