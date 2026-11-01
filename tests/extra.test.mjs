import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {calculateExtra as calc,parseGrades,parseTriples} from '../dist/assets/extra-math.js';
const catalog=JSON.parse(readFileSync(new URL('../scripts/extra-tools.json',import.meta.url)));
const defaults=Object.fromEntries(catalog.map(x=>[x.key,Object.fromEntries(x.fields.map(f=>[f.name,f.value??f.options[0][0]]))]));
const run=(k,changes={})=>calc(k,{...defaults[k],...changes});
const expected=[87.5,30,95,81,90,40,95,86,43,27,86,80,65,220/3,2,3.6,60,3.2,4.25,90,30,240,12.6];
catalog.forEach((x,i)=>test(`${x.title}: independent worked example`,()=>assert.ok(Math.abs(run(x.key).raw-expected[i])<1e-8)));
test('unreachable targets, already achieved targets and retake policies',()=>{
 assert.equal(run('attendance-target',{target:100}).raw,null);
 assert.equal(run('attendance-target',{attended:30,target:100}).raw,0);
 assert.equal(run('target-gpa',{target_gpa:4}).value,'Not reachable');
 assert.equal(run('gpa-credits',{future_gpa:3.5}).raw,null);
 assert.equal(run('gpa-credits',{target_gpa:2}).raw,0);
 assert.ok(Math.abs(run('retake-gpa',{policy:'both'}).raw-102/33)<1e-10);
 assert.equal(run('negative-marking',{correct:0,incorrect:20}).raw,-20);
});
test('reject invalid denominators, incompatible records and counts',()=>{
 const cases=[['remaining',{completed_weight:100}],['points-target',{remaining_points:0}],['assignment-target',{remaining_count:0}],['improvement',{current_grade:0,old_score:100}],['drop-lowest',{drop_count:4}],['must-pass',{final_weight:0}],['two-part',{part_one_weight:100}],['test-category',{current_grade:0}],['negative-marking',{correct:20,incorrect:1}],['minimum-correct',{total_questions:1.5}],['rubric',{rows:'8,10,50'}],['rubric',{rows:'0,0,100'}],['statistics',{grades:''}],['percentile',{equal:0}],['attendance',{attended:31}],['attendance-target',{target:0}],['target-gpa',{next_credits:0}],['gpa-credits',{credit_increment:0}],['retake-gpa',{course_credits:31}],['weighted-gpa',{rows:'4,0,1'}],['study-time',{days:0}],['reading-time',{words_per_minute:0}],['reading-speed',{minutes:0,seconds:0}],['exam-time',{review_minutes:120}]];
 for(const [k,v] of cases)assert.throws(()=>run(k,v),undefined,k);
 assert.throws(()=>parseGrades('NaN'));assert.throws(()=>parseTriples('1,,3'));
});
test('attendance minima and GPA credit targets satisfy their defining inequality',()=>{
 for(let held=1;held<=40;held++)for(let attended=0;attended<=held;attended++){
 const n=run('attendance-target',{classes_held:held,attended,target:75}).raw;
 assert.ok((attended+n)/(held+n)>=.75-1e-12);
 if(n>0)assert.ok((attended+n-1)/(held+n-1)<.75);
 }
 for(const target of [3.1,3.2,3.3,3.4,3.5]){const n=run('gpa-credits',{target_gpa:target,credit_increment:3}).raw;assert.ok((180+4*n)/(60+n)>=target-1e-12);if(n>0)assert.ok((180+4*(n-3))/(60+n-3)<target);}
});
