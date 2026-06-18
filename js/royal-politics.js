(function(){
'use strict';
const STORE='valeEmpires.royalPolitics';
const LAST_EVENT_LIMIT=12;
const clamp=(v,min=0,max=100)=>Math.max(min,Math.min(max,Number(v)||0));
const $=id=>document.getElementById(id);
function lang(){return localStorage.getItem('valeEmpires.language')||document.documentElement.lang||'pt-BR'}
const L={
 'pt-BR':{title:'Conselho Real',subtitle:'Sucessão dinástica, legitimidade, conselheiros e eventos políticos.',dynasty:'Dinastia',legitimacy:'Legitimidade',authority:'Autoridade',nobles:'Nobreza',clergy:'Clero',people:'Povo',heir:'Herdeiro',succession:'Lei de sucessão',council:'Conselheiros Reais',events:'Eventos do Reino',close:'VOLTAR',holdCourt:'REALIZAR CORTE',feast:'BANQUETE REAL',parade:'DESFILE MILITAR',codify:'CODIFICAR SUCESSÃO',assign:'Nomear',remove:'Remover',stable:'Reino estável',fragile:'Legitimidade frágil',crisis:'Crise política',saved:'Conselho Real atualizado',insufficient:'Recursos insuficientes',treasury:'Efeito no reino', export:'EXPORTAR POLÍTICA'},
 'en-US':{title:'Royal Council',subtitle:'Dynastic succession, legitimacy, advisors and political events.',dynasty:'Dynasty',legitimacy:'Legitimacy',authority:'Authority',nobles:'Nobility',clergy:'Clergy',people:'Commoners',heir:'Heir',succession:'Succession law',council:'Royal Advisors',events:'Realm Events',close:'BACK',holdCourt:'HOLD COURT',feast:'ROYAL FEAST',parade:'MILITARY PARADE',codify:'CODIFY SUCCESSION',assign:'Assign',remove:'Remove',stable:'Stable realm',fragile:'Fragile legitimacy',crisis:'Political crisis',saved:'Royal Council updated',insufficient:'Insufficient resources',treasury:'Realm effect', export:'EXPORT POLITICS'},
 'es-ES':{title:'Consejo Real',subtitle:'Sucesión dinástica, legitimidad, consejeros y eventos políticos.',dynasty:'Dinastía',legitimacy:'Legitimidad',authority:'Autoridad',nobles:'Nobleza',clergy:'Clero',people:'Pueblo',heir:'Heredero',succession:'Ley de sucesión',council:'Consejeros Reales',events:'Eventos del Reino',close:'VOLVER',holdCourt:'CELEBRAR CORTE',feast:'BANQUETE REAL',parade:'DESFILE MILITAR',codify:'CODIFICAR SUCESIÓN',assign:'Asignar',remove:'Remover',stable:'Reino estable',fragile:'Legitimidad frágil',crisis:'Crisis política',saved:'Consejo Real actualizado',insufficient:'Recursos insuficientes',treasury:'Efecto en el reino', export:'EXPORTAR POLÍTICA'}
};
function t(){const k=lang();return L[k]||L['pt-BR']}
const advisors={
 chancellor:{id:'chancellor',name:'Beatriz de Alba',role:{'pt-BR':'Chanceler','en-US':'Chancellor','es-ES':'Canciller'},bonus:{legitimacy:1.4,nobles:1.1},icon:'assets/ui/icons-upgrade/others/icon-diplomacy.png'},
 marshal:{id:'marshal',name:'Rodrigo de Ferro',role:{'pt-BR':'Marechal','en-US':'Marshal','es-ES':'Mariscal'},bonus:{authority:1.5},icon:'assets/ui/icons-upgrade/military/icon-infantry.png'},
 treasurer:{id:'treasurer',name:'Afonso do Tesouro',role:{'pt-BR':'Tesoureiro','en-US':'Treasurer','es-ES':'Tesorero'},bonus:{gold:10},icon:'assets/ui/icons-upgrade/resources/icon-gold.png'},
 spymaster:{id:'spymaster',name:'Helena da Sombra',role:{'pt-BR':'Mestre de Espiões','en-US':'Spymaster','es-ES':'Maestra de Espías'},bonus:{crisis:-.18},icon:'assets/ui/icons-upgrade/interface/icon-messages.png'},
 steward:{id:'steward',name:'Tomás da Pedra',role:{'pt-BR':'Mordomo-Mor','en-US':'Steward','es-ES':'Mayordomo Mayor'},bonus:{people:1.15},icon:'assets/ui/icons-upgrade/construction/icon-build.png'}
};
const laws={
 primogeniture:{id:'primogeniture',label:{'pt-BR':'Primogenitura','en-US':'Primogeniture','es-ES':'Primogenitura'},desc:{'pt-BR':'Sucessão mais estável, porém rígida.','en-US':'Most stable but less flexible succession.','es-ES':'Sucesión más estable, pero rígida.'},legitimacy:4,authority:1},
 elective:{id:'elective',label:{'pt-BR':'Monarquia Eletiva','en-US':'Elective Monarchy','es-ES':'Monarquía Electiva'},desc:{'pt-BR':'Agrada nobres, mas reduz controle dinástico.','en-US':'Pleases nobles but weakens dynastic control.','es-ES':'Agrada a nobles, pero reduce control dinástico.'},nobles:6,legitimacy:-2},
 merit:{id:'merit',label:{'pt-BR':'Sucessão por Mérito','en-US':'Merit Succession','es-ES':'Sucesión por Mérito'},desc:{'pt-BR':'Fortalece autoridade e reduz crises de incompetência.','en-US':'Strengthens authority and reduces incompetence crises.','es-ES':'Fortalece la autoridad y reduce crisis de incompetencia.'},authority:5,people:2,nobles:-2}
};
function names(){return ['Ariano','Leonor','Mateus','Clara','Henrique','Isabel','Davi','Helena','Tomás','Sofia']}
function traits(){return ['Justo','Estrategista','Piedoso','Audaz','Diplomata','Construtor','Comerciante','Guardião']}
function defaultPolitics(){
 const profile=window.ValeEmpiresAPI?.getProfile?.()||{};
 const first=(profile.name||'Vale').split(/\s+/)[0];
 return {schema:1,updatedAt:new Date().toISOString(),dynastyName:`Casa de ${first}`,rulerName:profile.name||'Governante do Vale',rulerAge:32,heirName:names()[Math.floor(Math.random()*names().length)],heirAge:12+Math.floor(Math.random()*12),heirTrait:traits()[Math.floor(Math.random()*traits().length)],successionLaw:'primogeniture',legitimacy:72,authority:62,nobles:56,clergy:54,people:64,regency:false,council:{chancellor:null,marshal:null,treasurer:null,spymaster:null,steward:null},stats:{courts:0,feasts:0,parades:0,codified:0,events:0,crisesSolved:0,bonusesGranted:0},lastTick:Date.now(),events:[`Dinastia fundada por ${profile.name||'seu governante'}.`]};
}
function normalize(p){const d=defaultPolitics(),s=p&&typeof p==='object'?p:{};const out={...d,...s};out.council={...d.council,...(s.council||{})};out.stats={...d.stats,...(s.stats||{})};out.successionLaw=laws[out.successionLaw]?out.successionLaw:'primogeniture';for(const k of ['legitimacy','authority','nobles','clergy','people'])out[k]=clamp(out[k]);out.heirAge=Math.max(0,Math.min(80,Number(out.heirAge)||d.heirAge));out.rulerAge=Math.max(16,Math.min(90,Number(out.rulerAge)||d.rulerAge));out.events=Array.isArray(out.events)?out.events.slice(-LAST_EVENT_LIMIT):d.events;out.lastTick=Number(out.lastTick)||Date.now();return out}
function load(){try{return normalize(JSON.parse(localStorage.getItem(STORE)||'null'))}catch{return defaultPolitics()}}
function save(){politics.updatedAt=new Date().toISOString();politics.events=politics.events.slice(-LAST_EVENT_LIMIT);localStorage.setItem(STORE,JSON.stringify(politics));window.ValeEmpiresAPI?.saveQuiet?.();updateButton();}
let politics=load();
function status(message){window.ValeEmpiresAPI?.status?.(message)||console.info(message)}
function addEvent(message,type='info'){politics.events.push(message);politics.events=politics.events.slice(-LAST_EVENT_LIMIT);politics.stats.events++;const live=document.getElementById('royalEventsList');if(live)render();status(message)}
function councilScore(){return Object.values(politics.council).filter(Boolean).length}
function legitimacyState(){const x=(politics.legitimacy+politics.authority+politics.nobles+politics.people+politics.clergy)/5;if(x>=70)return{key:'stable',text:t().stable,cls:'ready'};if(x>=45)return{key:'fragile',text:t().fragile,cls:'warning'};return{key:'crisis',text:t().crisis,cls:'danger'}}
function tick(){
 const now=Date.now(), elapsed=Math.max(0,now-politics.lastTick); if(elapsed<1000)return; const steps=Math.min(90,Math.floor(elapsed/1000)); politics.lastTick=now;
 for(let i=0;i<steps;i++){
  const council=councilScore();
  politics.legitimacy=clamp(politics.legitimacy+(council>=3?.002:-.006)+(politics.people-50)*.00005);
  politics.authority=clamp(politics.authority+(politics.successionLaw==='merit'?.004:.001));
  politics.nobles=clamp(politics.nobles+(politics.successionLaw==='elective'?.004:-.001));
  politics.people=clamp(politics.people+(politics.legitimacy-50)*.00008);
  politics.clergy=clamp(politics.clergy+.0005);
 }
 if(Math.random()<Math.min(.08,steps*.0025))politicalEvent();
 save(); render();
}
function politicalEvent(){
 const loc=lang();const hasSpy=politics.council.spymaster; const roll=Math.random();
 if(politics.legitimacy<42&&roll<.55){politics.nobles=clamp(politics.nobles-5);politics.authority=clamp(politics.authority-4);addEvent(loc.startsWith('en')?'A noble faction questioned the succession.':loc.startsWith('es')?'Una facción noble cuestionó la sucesión.':'Uma facção nobre questionou a sucessão.','warning');return}
 if(!hasSpy&&roll<.35){politics.people=clamp(politics.people-4);politics.legitimacy=clamp(politics.legitimacy-3);addEvent(loc.startsWith('en')?'Rumors spread through the court unchecked.':loc.startsWith('es')?'Rumores se extendieron por la corte sin control.':'Boatos se espalharam pela corte sem controle.','warning');return}
 const reward=8+councilScore()*3;window.ValeEmpiresAPI?.addStock?.('gold',reward);politics.stats.bonusesGranted+=reward;addEvent(loc.startsWith('en')?`The court secured +${reward} gold through influence.`:loc.startsWith('es')?`La corte aseguró +${reward} de oro por influencia.`:`A corte garantiu +${reward} ouro por influência.`,'success')
}
function spend(cost){return window.ValeEmpiresAPI?.spend?.(cost)||false}
function decision(action){
 const loc=lang();
 if(action==='court'){
  if(!spend({gold:65})){status(t().insufficient+': 65 ouro');return}
  politics.legitimacy=clamp(politics.legitimacy+8);politics.nobles=clamp(politics.nobles+4);politics.authority=clamp(politics.authority+3);politics.stats.courts++;
  addEvent(loc.startsWith('en')?'Royal court held: legitimacy strengthened.':loc.startsWith('es')?'Corte celebrada: legitimidad fortalecida.':'Corte realizada: legitimidade fortalecida.');
 }
 if(action==='feast'){
  if(!spend({food:120,gold:40})){status(t().insufficient+': 120 alimento • 40 ouro');return}
  politics.people=clamp(politics.people+9);politics.clergy=clamp(politics.clergy+3);politics.legitimacy=clamp(politics.legitimacy+4);politics.stats.feasts++;
  addEvent(loc.startsWith('en')?'Royal feast improved public support.':loc.startsWith('es')?'El banquete real aumentó el apoyo popular.':'Banquete real aumentou o apoio popular.');
 }
 if(action==='parade'){
  if(!spend({gold:55,wood:30})){status(t().insufficient+': 55 ouro • 30 madeira');return}
  politics.authority=clamp(politics.authority+10);politics.nobles=clamp(politics.nobles+2);politics.stats.parades++;
  addEvent(loc.startsWith('en')?'Military parade increased royal authority.':loc.startsWith('es')?'El desfile militar aumentó la autoridad real.':'Desfile militar elevou a autoridade real.');
 }
 if(action==='codify'){
  if(!spend({gold:90,stone:80})){status(t().insufficient+': 90 ouro • 80 pedra');return}
  politics.legitimacy=clamp(politics.legitimacy+12);politics.authority=clamp(politics.authority+5);politics.stats.codified++;
  addEvent(loc.startsWith('en')?'Succession code signed and sealed.':loc.startsWith('es')?'Código sucesorio firmado y sellado.':'Código sucessório assinado e selado.');
 }
 save();render();
}
function setLaw(id){if(!laws[id])return;const law=laws[id];politics.successionLaw=id;politics.legitimacy=clamp(politics.legitimacy+(law.legitimacy||0));politics.authority=clamp(politics.authority+(law.authority||0));politics.nobles=clamp(politics.nobles+(law.nobles||0));politics.people=clamp(politics.people+(law.people||0));addEvent((lang().startsWith('en')?'Succession changed to ':lang().startsWith('es')?'Sucesión cambiada a ':'Sucessão alterada para ')+(law.label[lang()]||law.label['pt-BR']));save();render()}
function assign(slot,id){if(!advisors[id])return;for(const s of Object.keys(politics.council)){if(politics.council[s]===id)politics.council[s]=null}politics.council[slot]=id;politics.legitimacy=clamp(politics.legitimacy+1);addEvent(`${advisors[id].name} ${lang().startsWith('en')?'joined the Royal Council':lang().startsWith('es')?'entró en el Consejo Real':'entrou no Conselho Real'}`);save();render()}
function metric(label,value,cls=''){return `<div class="royal-metric ${cls}"><span>${label}</span><b>${Math.round(value)}%</b><i style="width:${clamp(value)}%"></i></div>`}
function advisorCard(slot){const id=politics.council[slot],adv=id&&advisors[id],label={chancellor:'Chanceler',marshal:'Marechal',treasurer:'Tesoureiro',spymaster:'Espiões',steward:'Mordomo'}[slot]||slot;if(adv)return `<div class="royal-advisor selected"><img src="${adv.icon}" alt=""><div><strong>${adv.name}</strong><span>${adv.role[lang()]||adv.role['pt-BR']} • ${label}</span></div><button data-remove-advisor="${slot}">×</button></div>`;return `<div class="royal-advisor"><img src="assets/ui/icons-upgrade/status/icon-blocked.png" alt=""><div><strong>${label}</strong><span>${lang().startsWith('en')?'Vacant':lang().startsWith('es')?'Vacante':'Vago'}</span></div></div>`}
function render(){const box=$('royalCouncilBody');if(!box)return;const T=t(),state=legitimacyState(),law=laws[politics.successionLaw];box.innerHTML=`<div class="royal-banner ${state.cls}"><img src="assets/ui/icons-upgrade/others/icon-heroes.png" alt=""><div><small>${T.dynasty.toUpperCase()}</small><strong>${politics.dynastyName}</strong><span>${state.text} • ${T.legitimacy} ${Math.round(politics.legitimacy)}%</span></div><b>${Math.round((politics.legitimacy+politics.authority)/2)}%</b></div><div class="royal-layout"><section class="royal-card"><h3>${T.dynasty}</h3>${metric(T.legitimacy,politics.legitimacy)}${metric(T.authority,politics.authority)}${metric(T.nobles,politics.nobles)}${metric(T.clergy,politics.clergy)}${metric(T.people,politics.people)}<div class="royal-actions"><button data-royal-action="court">${T.holdCourt}<small>65 ouro</small></button><button data-royal-action="feast">${T.feast}<small>120 alimento • 40 ouro</small></button><button data-royal-action="parade">${T.parade}<small>55 ouro • 30 madeira</small></button><button data-royal-action="codify">${T.codify}<small>90 ouro • 80 pedra</small></button></div></section><section class="royal-card"><h3>${T.heir}</h3><div class="royal-heir"><img src="assets/ui/icons-upgrade/others/icon-heroes.png" alt=""><div><strong>${politics.heirName}</strong><span>${politics.heirAge} anos • ${politics.heirTrait}</span></div></div><h3>${T.succession}</h3><div class="royal-laws">${Object.values(laws).map(x=>`<button data-royal-law="${x.id}" class="${x.id===politics.successionLaw?'selected':''}"><strong>${x.label[lang()]||x.label['pt-BR']}</strong><span>${x.desc[lang()]||x.desc['pt-BR']}</span></button>`).join('')}</div></section><section class="royal-card"><h3>${T.council}</h3><div class="royal-advisors">${Object.keys(politics.council).map(advisorCard).join('')}</div><div class="royal-assign-grid">${Object.values(advisors).map(a=>`<button data-assign-any="${a.id}"><img src="${a.icon}" alt=""><strong>${a.name}</strong><span>${a.role[lang()]||a.role['pt-BR']}</span></button>`).join('')}</div></section></div><section class="royal-card royal-events"><h3>${T.events}</h3><div id="royalEventsList">${politics.events.slice().reverse().map(e=>`<p>${e}</p>`).join('')}</div></section>`;box.querySelectorAll('[data-royal-action]').forEach(b=>b.onclick=()=>decision(b.dataset.royalAction));box.querySelectorAll('[data-royal-law]').forEach(b=>b.onclick=()=>setLaw(b.dataset.royalLaw));box.querySelectorAll('[data-remove-advisor]').forEach(b=>b.onclick=()=>{politics.council[b.dataset.removeAdvisor]=null;save();render()});box.querySelectorAll('[data-assign-any]').forEach(b=>{b.onclick=()=>{const empty=Object.keys(politics.council).find(k=>!politics.council[k])||'chancellor';assign(empty,b.dataset.assignAny)}});}
function open(){ensureOverlay();tick();render();$('royalCouncilOverlay').classList.remove('hidden');$('royalCouncilOverlay').setAttribute('aria-hidden','false')}
function close(){const el=$('royalCouncilOverlay');if(el){el.classList.add('hidden');el.setAttribute('aria-hidden','true')}}
function updateButton(){const btn=$('btnRoyalCouncilPanel');if(!btn)return;const state=legitimacyState();btn.dataset.tooltip=`${t().title}: ${state.text} (${Math.round(politics.legitimacy)}%)`;btn.classList.toggle('danger',state.cls==='danger');btn.classList.toggle('ready',state.cls==='ready')}
function ensureOverlay(){if($('royalCouncilOverlay'))return;const el=document.createElement('section');el.id='royalCouncilOverlay';el.className='royal-overlay hidden';el.setAttribute('aria-hidden','true');el.innerHTML=`<div class="royal-backdrop"></div><div class="royal-shell" role="dialog" aria-modal="true"><header class="royal-header"><img src="assets/ui/icons-upgrade/others/icon-heroes.png" alt=""><div><small>VALE EMPIRES</small><h2 id="royalCouncilTitle">${t().title}</h2><p id="royalCouncilSubtitle">${t().subtitle}</p></div><button id="royalExport">${t().export}</button><button id="royalClose">${t().close}</button></header><div id="royalCouncilBody"></div></div>`;document.body.appendChild(el);el.querySelector('.royal-backdrop').onclick=close;el.querySelector('#royalClose').onclick=close;el.querySelector('#royalExport').onclick=exportPolitics;}
function exportPolitics(){const blob=new Blob([JSON.stringify(politics,null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='vale-empires-conselho-real.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),5000)}
function bind(){const btn=$('btnRoyalCouncilPanel');if(btn)btn.onclick=open;ensureOverlay();updateButton();setInterval(()=>{tick();updateButton()},10000);document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='hidden')save()});}
function restore(data){if(data){politics=normalize(data);save();updateButton();}}
function newReign(){const p=window.ValeEmpiresAPI?.getProfile?.();politics=defaultPolitics();if(p?.name){politics.rulerName=p.name;politics.dynastyName=`Casa de ${p.name.split(/\s+/)[0]}`;}save();updateButton();}
window.ValeRoyalPolitics={open,serialize:()=>normalize(politics),restore,newReign,addEvent,updateButton};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind);else bind();
})();
