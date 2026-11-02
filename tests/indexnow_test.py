import sys,unittest,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from submit_indexnow import select_urls,changed_urls,sitemap_urls,BASE
class IndexNowSelection(unittest.TestCase):
 def test_bootstrap_and_manual_use_full_sitemap(self):
  urls=[BASE+'/',BASE+'/guides/']
  self.assertEqual(select_urls(urls,[],True),urls)
  self.assertEqual(select_urls(urls,[],event='workflow_dispatch'),urls)
 def test_normal_release_only_changed_pages(self):
  self.assertEqual(select_urls([BASE+'/'],['dist/guides/example/index.html','dist/assets/styles.css']),[BASE+'/guides/example/'])
 def test_home_deleted_and_duplicate_paths(self):
  self.assertEqual(changed_urls(['dist/index.html','dist/removed/index.html','dist/removed/index.html','dist/404/index.html']),[BASE+'/',BASE+'/removed/'])
 def test_noncontent_and_invalid_paths_not_sent(self):
  self.assertEqual(changed_urls(['site-config.json','dist/../example/index.html','dist/assets/app.js']),[])
 def test_current_sitemap_is_valid(self):
  self.assertEqual(len(sitemap_urls(Path(__file__).resolve().parents[1]/'dist/sitemap.xml')),58)
if __name__=='__main__':unittest.main()
