const fs=require('fs'),vm=require('vm');
const listeners={},storage=new Map();
const context={
 window:{VALE_BUILD:{buildId:'VE-3.9.0-F33',version:'v3.9.0'},addEventListener:(n,fn)=>{listeners[n]=fn}},
 navigator:{userAgent:'node-audit',language:'pt-BR',platform:'node',onLine:true},
 localStorage:{getItem:k=>storage.get(k)||null},document:{fullscreenElement:null,getElementById:()=>null,addEventListener:()=>{},body:{appendChild:()=>{}}},
 matchMedia:()=>({matches:false}),innerWidth:915,innerHeight:412,devicePixelRatio:1,Image:function(){},Blob:function(){this.size=0},URL:{createObjectURL:()=>'',revokeObjectURL:()=>{}},setTimeout,console
};
vm.createContext(context);vm.runInContext(fs.readFileSync(__dirname+'/../js/release-guard.js','utf8'),context);
const old={schemaVersion:12,profile:{name:'Teste',eraPack:'medieval'},camera:{x:0,y:0},buildings:[],units:[],enemies:[],urbanSiege:{city:{owner:'player'}}};
const migrated=context.window.VALE_RELEASE_GUARD.migrateSave(old);
if(migrated.schemaVersion!==13)throw new Error('schema não migrou para 13');
if(migrated.cityAdministration!==null)throw new Error('fallback cityAdministration inválido');
if(migrated.eraPack!=='medieval')throw new Error('eraPack inválido');
console.log(JSON.stringify({ok:true,schemaVersion:migrated.schemaVersion,cityAdministration:migrated.cityAdministration,migratedFrom:migrated.migratedFrom}));
