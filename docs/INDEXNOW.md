# IndexNow integration

Configured after owner request on2November2026. An independently generated ownership key is served as a UTF-8 root text file. This is unrelated to the uploaded SSL private key; that file is not read, copied or published.

After successful GitHub Pages deployment, the notifier first fetches the live HTTPS key file and verifies its content, then POSTs to https://api.indexnow.org/indexnow. Initial setup submits the58 canonical sitemap URLs. Later pushes notify changed or removed tracked dist HTML pages only; manual workflow runs can request a full refresh. Checkout fetches the parent commit for change selection. A future release must include its generated dist changes, as this repository does today.

A notification failure is reported in the workflow step without taking the already-deployed website offline. The script does not silently retry API errors. An HTTP200 confirms receipt;202 means accepted with key validation pending. Neither confirms actual indexing. A successful key check and API result are written to the Actions summary. No Bing account API secret, analytics or frontend request script is introduced.

Official protocol reference: https://www.indexnow.org/documentation

Google Search Console and Bing sitemap submissions remain separate. GSC accepted the updated sitemap and two URL-inspection requests; Bing accepted58 direct URL submissions and is processing the sitemap.
