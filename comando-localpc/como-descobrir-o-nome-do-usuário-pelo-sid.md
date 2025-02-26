# Como descobrir o nome do usuário pelo SID?

Date: 2017-02-14 13:17:34

Categories: Comando local/PC, Windows Server 2003, Windows Server 2008, Windows Server 2008 R2, Windows Server 2012

---

<p style="text-align: justify;">Como descobrir o nome do usuário se eu tiver apenas o SID? já pensou em fazer cálculos matemáticos pra conseguir esse resultado? Espero que não! Por isso mesmo, basta usar o comando abaixo para conseguir o resultado que procura.</p>
<p>&nbsp;</p>
<blockquote>
<pre>$objSID = New-Object System.Security.Principal.SecurityIdentifier ("INSIRA O SID AQUI")
$objUser = $objSID.Translate( [System.Security.Principal.NTAccount])
$objUser.Value</pre>
</blockquote>
