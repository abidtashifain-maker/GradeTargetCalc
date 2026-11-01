import * as math from './math.js';
const theme=document.querySelector('.theme');
let preference;
try{preference=localStorage.getItem('gtc-theme');}catch{}
const dark=preference?preference==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
function applyTheme(value){document.body.classList.toggle('dark',value);if(theme){theme.setAttribute('aria-pressed',String(value));theme.setAttribute('aria-label',`Switch to ${value?'light':'dark'} mode`);}}
applyTheme(dark);
theme?.addEventListener('click',()=>{const d=!document.body.classList.contains('dark');applyTheme(d);try{localStorage.setItem('gtc-theme',d?'dark':'light');}catch{}});
const fmt=n=>n.toFixed(2);
for(const form of document.querySelectorAll('[data-calculator]')){
 const kind=form.dataset.calculator,result=form.querySelector('.result');
 let nextRow=1;
 const empty=()=>{result.classList.remove('error');result.replaceChildren();const label=document.createElement('span');label.className='result-label';label.textContent='YOUR RESULT';const strong=document.createElement('strong');strong.textContent='Let’s work it out.';const p=document.createElement('p');p.textContent='Select Calculate to see the result.';result.append(label,strong,p);};
 function renumber(){form.querySelectorAll('.data-row').forEach((r,i)=>{const inputs=r.querySelectorAll('input');inputs[0].setAttribute('aria-label',`${kind==='gpa'?'Grade points':'Score percentage'}, row ${i+1}`);inputs[1].setAttribute('aria-label',`${kind==='gpa'?'Credits':'Weight'}, row ${i+1}`);r.querySelector('button').setAttribute('aria-label',`Remove row ${i+1}`);});}
 function row(a='',b=''){
  const box=form.querySelector('[data-rows]');if(!box)return;
  const n=nextRow++,isGpa=kind==='gpa';
  const div=document.createElement('div');div.className='data-row';
  const label1=document.createElement('label');label1.className='field';label1.textContent=isGpa?'Grade points': 'Score (%)';
  const input1=document.createElement('input');input1.type='number';input1.step='any';input1.min='0';input1.max=isGpa?form.elements.scale.value:'100';input1.required=true;input1.value=a;input1.setAttribute('aria-label',`${isGpa?'Grade points':'Score percentage'}, row ${n}`);label1.append(input1);
  const label2=document.createElement('label');label2.className='field';label2.textContent=isGpa?'Credits':form.elements.weightMode.value==='credits'?'Credits / weight':'Weight (%)';
  const input2=document.createElement('input');input2.type='number';input2.step='any';input2.min='0.000001';input2.max='10000';input2.required=true;input2.value=b;input2.setAttribute('aria-label',`${isGpa?'Credits':'Weight'}, row ${n}`);label2.append(input2);
  const remove=document.createElement('button');remove.type='button';remove.className='remove';remove.textContent='×';remove.setAttribute('aria-label',`Remove row ${n}`);remove.addEventListener('click',()=>{div.remove();renumber();empty();form.querySelector('[data-add]').focus();});
  div.append(label1,label2,remove);box.append(div);renumber();return input1;
 }
 function samples(){const box=form.querySelector('[data-rows]');if(!box)return;box.replaceChildren();nextRow=1;if(kind==='weighted'){row(80,40);row(70,60);}else {row(4,3);row(3,4);row(2,2);}}
 samples();
 form.querySelector('[data-add]')?.addEventListener('click',()=>{const input=row();input?.focus();empty();});
 function updateMode(){if(kind==='final'){const target=form.elements.target;target.closest('label').firstChild.textContent=form.elements.mode.value==='overall'?'Final exam score (%)':'Target course grade (%)';target.setAttribute('aria-label',form.elements.mode.value==='overall'?'Final exam score (%)':'Target course grade (%)');}if(kind==='weighted'){form.querySelectorAll('.data-row').forEach(r=>{r.children[1].firstChild.textContent=form.elements.weightMode.value==='credits'?'Credits / weight':'Weight (%)';});}if(kind==='gpa'){form.querySelectorAll('.data-row').forEach(r=>r.querySelector('input').max=form.elements.scale.value);}}
 form.addEventListener('input',()=>{updateMode();empty();});
 form.addEventListener('change',e=>{if(e.target.tagName==='SELECT'){updateMode();empty();}});
 form.addEventListener('reset',()=>{setTimeout(()=>{samples();updateMode();empty();},0);});
 function show(title,value,message){result.classList.remove('error');result.replaceChildren();const l=document.createElement('span');l.className='result-label';l.textContent=title;const v=document.createElement('strong');v.textContent=value;const p=document.createElement('p');p.textContent=message;result.append(l,v,p);}
 function table(headers,rows){const t=document.createElement('table');t.className='scenarios';const caption=document.createElement('caption');caption.textContent='What-if final exam outcomes';t.append(caption);const head=document.createElement('thead'),tr=document.createElement('tr');headers.forEach(x=>{const th=document.createElement('th');th.scope='col';th.textContent=x;tr.append(th);});head.append(tr);t.append(head);const body=document.createElement('tbody');rows.forEach(row=>{const tr=document.createElement('tr');row.forEach(x=>{const td=document.createElement('td');td.textContent=x;tr.append(td);});body.append(tr);});t.append(body);result.append(t);}
 form.addEventListener('submit',e=>{e.preventDefault();const v=Object.fromEntries(new FormData(form));try{
  if(kind==='final'){
   if(v.mode==='overall'){const n=math.finalOverall(v.current,v.target,v.weight);show('OVERALL COURSE GRADE',fmt(n)+'%',`Your non-final work contributes ${fmt(Number(v.current)*(1-Number(v.weight)/100))} points; your exam contributes ${fmt(Number(v.target)*Number(v.weight)/100)} points.`);}
   else {const n=math.finalNeeded(v.current,v.target,v.weight);show('MINIMUM SCORE NEEDED',fmt(Math.max(0,math.minimumDisplayed(n)))+'%',n>100?'This target is not reachable with an exam capped at 100%. Recheck inputs or try a lower target.':n<=0?'Even a zero would meet this weighted-average target. Separate exam-pass or attendance requirements can still apply.':'Aim at or above this score. The minimum is rounded upward to two decimals; check course rounding and pass rules.');
   table(['Exam score','Course grade'],[50,60,70,80,90,100].map(x=>[x+'%',fmt(math.finalOverall(v.current,x,v.weight))+'%']));}
  }else if(kind==='weighted'||kind==='gpa'){
   const rows=[...form.querySelectorAll('.data-row')].map(r=>[...r.querySelectorAll('input')].map(i=>i.value));
   if(kind==='weighted'){const r=math.weighted(rows,v.weightMode);show(v.weightMode==='percent'&&r.weight<100-1e-8?'CURRENT AVERAGE OF COMPLETED WORK':'WEIGHTED AVERAGE',fmt(r.average)+'%',v.weightMode==='percent'?`Completed weight: ${fmt(r.weight)}%. Course contribution: ${fmt(r.contribution)} percentage points. Ungraded weight: ${fmt(r.remaining)}%.`:`Calculated across ${fmt(r.weight)} total credits / relative weight. This is not an official degree classification.`);}
   else{const r=math.gpa(rows,v.scale);show('SEMESTER GPA',fmt(r.value),`${fmt(r.points)} quality points ÷ ${fmt(r.credits)} GPA-bearing credits, on your selected ${v.scale}-point scale.`);}
  }else if(kind==='cumulative'){const r=math.cumulative(v.oldGpa,v.oldCredits,v.newGpa,v.newCredits,v.scale);show('CUMULATIVE GPA ESTIMATE',fmt(r.value),`${fmt(r.points)} estimated quality points ÷ ${fmt(r.credits)} total GPA-bearing credits. Rounded input GPAs can reduce precision.`);
  }else if(kind==='percentage'){const r=math.percentage(v.earned,v.possible);show('GRADE PERCENTAGE',fmt(r)+'%',`${v.earned} ÷ ${v.possible} × 100 = ${fmt(r)}%. Use your institution’s table for a letter grade.`);
  }else if(kind==='test'){const r=math.testScore(v.total,v.wrong);show('TEST SCORE',fmt(r.percent)+'%',`${r.correct} correct out of ${v.total} equally weighted questions. ${v.wrong} incorrect or unanswered.`);
  }else if(kind==='average'){const values=v.grades.trim()?v.grades.trim().split(/[,\s]+/):[];const r=math.average(values);show('EQUALLY WEIGHTED AVERAGE',fmt(r.value)+'%',`${r.count} grades. Lowest: ${fmt(r.min)}%. Highest: ${fmt(r.max)}%. All entered grades count equally.`);}
 }catch(err){show('CHECK YOUR INPUTS','Please check these values.',err.message);result.classList.add('error');}});
}
