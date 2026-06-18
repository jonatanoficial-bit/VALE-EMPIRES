const fs=require('fs'),vm=require('vm');
const listeners={};
const storage=new Map();
const context={
 window:{VALE_BUILD:{buildId:'VE-3.8.0-F32',version:'v3.8.0'},addEventListener:(n,fn)=>{listeners[n]=fn}},
 navigator:{userAgent:'node-audit',language:'pt-BR',platform:'node',onLine:true},
 localStorage:{getItem:k=>storage.get(k)||null},
 document:{fullscreenElement:null,getElementById:()=>null,addEventListener:()=>{},body:{appendChild:()=>{}}},
 matchMedia:()=>({matches:false}),innerWidth:915,innerHeight:412,devicePixelRatio:1,
 Image:function(){},Blob:function(){this.size=0},URL:{createObjectURL:()=>'',revokeObjectURL:()=>{}},setTimeout,console
};
vm.createContext(context);
vm.runInContext(fs.readFileSync(__dirname+'/../js/release-guard.js','utf8'),context);
const old={schemaVersion:11,profile:{name:'Teste',eraPack:'medieval'},camera:{x:0,y:0},buildings:[],units:[],enemies:[],coastalSiege:{port:{owner:'player'}}};
const migrated=context.window.VALE_RELEASE_GUARD.migrateSave(old);
if(migrated.schemaVersion!==12)throw new Error('schema não migrou');
if(migrated.urbanSiege!==null)throw new Error('urbanSiege fallback inválido');
if(migrated.eraPack!=='medieval')throw new Error('eraPack inválido');
console.log(JSON.stringify({ok:true,schemaVersion:migrated.schemaVersion,urbanSiege:migrated.urbanSiege,migratedFrom:migrated.migratedFrom}));
