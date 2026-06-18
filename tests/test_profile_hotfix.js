
const nodes={};
function node(id){return nodes[id]||(nodes[id]={id,src:'',alt:'',textContent:'',classList:{remove(){this.removed=true}},dataset:{},style:{setProperty(){}}})}
const document={documentElement:{style:{setProperty(k,v){this[k]=v}}},getElementById:node};
const $=node;
const state={profile:{name:'Teste Hotfix',avatar:'governor',nation:'england',eraPack:'medieval'},periodPack:'medieval'};
const AVATAR_DEFS={governor:{src:'avatar.png',label:'Governante'}};
const NATION_DEFS={england:{flag:'flag.png',label:'Reino da Inglaterra',sigil:'♜',color:'#254f86',playstyle:'Defesa',uniqueTech:{key:'x',label:'Tech'}}};
function normalizeProfile(p){return p}
function loadProfile(){return null}
function nationById(id){return NATION_DEFS[id]}
function eraPackById(id){return {id:'medieval',label:'Era Medieval'}}
function normalizeEraPack(id){return id}
function updateCivilizationUI(){nodes._civUpdated=true}
function updateProfileHUD(){const p=normalizeProfile(state.profile||loadProfile(),true),a=AVATAR_DEFS[p.avatar]||AVATAR_DEFS.governor,n=nationById(p.nation),pack=eraPackById(p.eraPack||state.periodPack||'medieval');state.profile=p;state.periodPack=normalizeEraPack(pack.id,true);document.documentElement.style.setProperty('--nation-accent',n.color);if($('gameScreen'))$('gameScreen').dataset.nation=p.nation;if($('profileHudAvatar')){$('profileHudAvatar').src=a.src;$('profileHudAvatar').alt=a.label||'Governante'}if($('profileHudFlag')){$('profileHudFlag').src=n.flag;$('profileHudFlag').alt=`Bandeira de ${n.label}`}if($('profileHudName'))$('profileHudName').textContent=p.name;if($('profileHudNation'))$('profileHudNation').textContent=`${n.sigil} ${n.label}`;if($('menuProfileAvatar')){$('menuProfileAvatar').src=a.src;$('menuProfileAvatar').alt=a.label||'Governante'}if($('menuProfileFlag')){$('menuProfileFlag').src=n.flag;$('menuProfileFlag').alt=`Bandeira de ${n.label}`}if($('menuProfileName'))$('menuProfileName').textContent=p.name;if($('menuProfileNation'))$('menuProfileNation').textContent=n.label;if($('menuProfilePeriod'))$('menuProfilePeriod').textContent=pack.label;if($('menuProfileSummary'))$('menuProfileSummary').classList.remove('hidden');updateCivilizationUI()}
updateProfileHUD();
const result={name:node('menuProfileName').textContent,nation:node('menuProfileNation').textContent,period:node('menuProfilePeriod').textContent,flag:node('menuProfileFlag').src,hudName:node('profileHudName').textContent,civ:!!nodes._civUpdated};
if(result.name!=='Teste Hotfix'||result.nation!=='Reino da Inglaterra'||result.period!=='Era Medieval'||result.flag!=='flag.png'||result.hudName!=='Teste Hotfix'||!result.civ)throw new Error(JSON.stringify(result));
console.log(JSON.stringify(result));
