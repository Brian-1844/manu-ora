// node test_porter.js [fichier] — porter chaque instrument, changer de finition, reposer, rechargement.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const p=await b.newPage({viewport:{width:390,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{if(localStorage.getItem('manuora.welcomed'))return;localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.instr',JSON.stringify({uke:{fin:'nat',day:''},toere:{fin:'nacre',day:'',owned:['nat','nacre']},pahu:{fin:'grav',day:''}}));localStorage.setItem('manuora.vivo',JSON.stringify({ofe:true,made:true,day:'',retry:''}));});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);const clear=()=>p.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});await clear();
await p.evaluate(()=>openInstr());console.log('boutons',await p.evaluate(()=>[...sheetInner.querySelectorAll('[data-carry]')].map(x=>x.dataset.carry).join()));
const zoom=async(n)=>{const r=await p.evaluate(()=>{const e=$('#bird').getBoundingClientRect();return {x:e.left-30,y:e.top-30,w:e.width+60,h:e.height+60};});await p.screenshot({path:O+n,clip:{x:Math.max(0,r.x),y:Math.max(0,r.y),width:r.w,height:r.h}});};
for(const id of ['uke','toere','pahu','vivo']){ await p.evaluate(id=>{openInstr();sheetInner.querySelector('[data-carry="'+id+'"]').click();},id); await clear(); await p.waitForTimeout(200); console.log(id,await p.evaluate(()=>[cfg.carry,!!$('#birdFlip .carry'),($('#birdFlip .carry')||{}).dataset?.id])); await zoom('carry_'+id+'.png'); }
await p.evaluate(()=>{openInstr();sheetInner.querySelector('[data-carry="vivo"]').click();});await clear();console.log('posé',await p.evaluate(()=>[cfg.carry,!!$('#birdFlip .carry')]));
await p.evaluate(()=>{openInstr();sheetInner.querySelector('[data-carry="toere"]').click();});await clear();await p.reload();await p.waitForTimeout(1500);console.log('après rechargement',await p.evaluate(()=>[cfg.carry,!!$('#birdFlip .carry')]));
await p.evaluate(()=>{renderBird();});console.log('après renderBird',await p.evaluate(()=>!!$('#birdFlip .carry')));
console.log('errs',errs);await b.close();})();
