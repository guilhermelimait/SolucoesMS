# Como exportar todos os usuários que estão com limite diferente de &#8220;unlimited&#8221;

Date: 2017-01-27 17:51:28

Categories: Exchange 2010

---

<p>Em uma nova pesquisa precisava exportar todos os usuários que estavam com limites de envio diferentes do padrão da TransportServer definida. Para isso, o comando abaixo foi utilizado:</p>
<blockquote>
<pre>Get-Mailbox -resultsize unlimited| Where-Object{$_.MaxSendSize -ne "unlimited" -or $_.MaxReceiveSize -ne "unlimited"} | Select-Object samaccountname, DisplayName,MaxSendSize,MaxReceiveSize | export-csv .\REPORT.csv</pre>
</blockquote>
