const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const O='/home/claude/work/';
// 1. first visit
let ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti',userAgent:'Mozilla/5.0 (Linux; Android 14) Chrome/126 Mobile'});let p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.goto('file:///tmp/claude-0/d_m.html');await p.waitForTimeout(1800);
console.log('welcome',await p.evaluate(()=>[sheetInner.querySelector('h2').textContent,!!$('#w0Inst'),!!$('#w0Go')]));
await p.screenshot({path:O+'d_wel.png'});
await p.evaluate(()=>$('#w0Inst').click());await p.waitForTimeout(300);await p.screenshot({path:O+'d_wel2.png'});
await p.evaluate(()=>$('#w0Go').click());await p.waitForTimeout(300);console.log('step1',await p.evaluate(()=>sheetInner.querySelector('h2').textContent));
await p.evaluate(()=>$('#wNext').click());await p.waitForTimeout(200);await p.evaluate(()=>$('#wBack').click());await p.waitForTimeout(200);console.log('back',await p.evaluate(()=>sheetInner.querySelector('h2').textContent));
await ctx.close();
// 2. dock
ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});p=await ctx.newPage();p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.cfg',JSON.stringify(Object.assign(JSON.parse(localStorage.getItem('manuora.cfg')||'{}'),{night:'off'})));});
await p.goto('file:///tmp/claude-0/d.html');await p.waitForTimeout(1500);
await p.evaluate(()=>{try{closeRing()}catch(e){};closeSheet();cfg.night='off';renderNight();setPlace('none');bubbleEl.classList.remove('show')});
console.log('dock none',await p.evaluate(()=>[...document.querySelectorAll('#qDock>button')].map(x=>x.textContent)));
await p.click('#qPlace');await p.waitForTimeout(200);await p.screenshot({path:O+'d_pick.png'});
for(const k of ['vai','tai','oire','haapii']){ if(!(await p.$('.qplaces'))) await p.click('#qPlace'); await p.click(`.qplaces [data-pl="${k}"]`);await p.waitForTimeout(500);
  const acts=await p.evaluate(()=>[...document.querySelectorAll('#qDock [data-a]')].map(x=>x.textContent+(x.classList.contains('lock')?'*':'')));
  await p.evaluate(()=>{try{closeRing()}catch(e){};bubbleEl.classList.remove('show')});await p.screenshot({path:O+'d_'+k+'.png'});
  const titles=[];for(let i=0;i<acts.length;i++){ await p.click(`#qDock [data-a="${i}"]`);await p.waitForTimeout(350);titles.push(await p.evaluate(()=>$('#sheet').hidden?'(toast)':sheetInner.querySelector('h2').textContent));await p.evaluate(()=>{try{bkQuit()}catch(e){};closeSheet()});await p.waitForTimeout(150);}
  console.log(k,curP=await p.evaluate(()=>curPlace),acts,titles);}
// outside tap closes popover; left corner moves dock right
await p.click('#qPlace');await p.mouse.click(300,500);await p.waitForTimeout(150);console.log('popover closed',!(await p.$('.qplaces')));
await p.evaluate(()=>{cfg.corner='tl';dockRender()});console.log('right',await p.evaluate(()=>$('#qDock').classList.contains('right')));
console.log('errs',errs);await b.close();})();
