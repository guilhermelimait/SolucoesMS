# Como desabilitar o MyAnalytics do usuário?

Date: 2020-01-13 17:38:08

Categories: MyAnalytics, O365

---

<p>Olá pessoal, tudo bem? Mais uma demanda interessante dos usuários apareceu por aqui. Nesse caso, os usuários estavam reclamando do &#8220;SPAM&#8221; qu e é o MyAnalytics toda segunda-feira dizendo como foi ou não produtiva a sua última semana. Como desabilitar isso?</p>
<p>Para um ou poucos usuários:</p>
<p>1- Faça logon no <a href="http://portal.office.com">portal.office.com</a><br />
2- Clique em ADMIN<br />
3- Clique em SETTINGS<br />
4- Clique em SERVICES &amp; ADD-INS<br />
5- Clique em MyAnalytics<br />
6- Desabilite o INSIGHTS DASHBOARD, WEEKLY EMAIL INSIGHTS EMAIL e/ou INSIGHTS OUTLOOK ADD-IN</p>
<blockquote><p>Para desabilitar para todos os usuários com um licenciamento específico:</p>
<pre><span style="color: #ff0000;"><span class="hljs-variable">$acctSKU</span>=<span class="hljs-string">"<strong>MINHAEMPRESA:ENTERPRISEPACK</strong>)"</span> </span>
<span style="color: #ff0000;"><span class="hljs-variable">$AllLicensed</span> = <span class="hljs-pscommand">Get-MsolUser</span><span class="hljs-parameter"> -All</span> | Where {<span class="hljs-variable">$_</span>.isLicensed<span class="hljs-nomarkup"> -eq</span> <span class="hljs-literal">$true</span><span class="hljs-parameter"> -and</span> <span class="hljs-variable">$_</span>.licenses[<span class="hljs-number">0</span>].AccountSku.SkuPartNumber<span class="hljs-nomarkup"> -eq</span> (<span class="hljs-variable">$acctSKU</span>).Substring(<span class="hljs-variable">$acctSKU</span>.IndexOf(<span class="hljs-string">":"</span>)+<span class="hljs-number">1</span>, <span class="hljs-variable">$acctSKU</span>.Length-<span class="hljs-variable">$acctSKU</span>.IndexOf(<span class="hljs-string">":"</span>)-<span class="hljs-number">1</span>)} </span>
<span style="color: #ff0000;"><span class="hljs-variable">$AllLicensed</span> | <span class="hljs-keyword">ForEach</span> {<span class="hljs-pscommand">Set-MsolUserLicense</span><span class="hljs-parameter"> -UserPrincipalName</span> <span class="hljs-variable">$_</span>.UserPrincipalName<span class="hljs-parameter"> -LicenseOptions</span> <span class="hljs-variable">$LO</span>}</span></pre>
</blockquote>
<p>Na primeira semana, o e-mail deixará de ser enviado. 🙂</p>
<p>Fontes:</p>
<p><a href="https://www.urtech.ca/2019/11/solved-what-is-office365-myanalytics-how-can-i-disable-the-emails/" target="_blank" rel="noopener noreferrer">URTECH</a><br />
<a href="https://docs.microsoft.com/en-us/workplace-analytics/myanalytics/overview/privacy-guide" target="_blank" rel="noopener noreferrer">MICROSOFT</a></p>
