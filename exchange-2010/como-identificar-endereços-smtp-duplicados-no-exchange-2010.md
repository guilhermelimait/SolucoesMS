# Como identificar endereços SMTP duplicados no Exchange 2010?

Date: 2013-12-06 12:45:49

Categories: Exchange 2010

---

<p>Estava com esse desafio de encontrar todos os endereços duplicados existentes na floresta do Exchange 2010. Depois de procurar por todos os lugares consegui um pequeno script que é efetivo em seus resultados.</p>
<blockquote>
<pre>$ht = @{}
 Get-mailcontact -resultsize unlimited|
 Select PrimarySmtpAddress,distinguishedName |
 foreach {$ht[$_.PrimarySmtpAddress] += @($_.DistinguishedName, $_.Alias, $_.mail, $_.samaccountname)
 }
 ]
 $ht.keys |
 foreach {
 if (($ht[$_]).count -gt 1) {
 $_
 $ht[$_]
 "'n"
 }
 }</pre>
</blockquote>
<p>Salve em um arquivo chamado duplicateItems.ps1<br />
Recomendo ainda utilizar o seguinte comando para que possa exportar os dados em um arquivo.</p>
<blockquote>
<pre>[PS] C:\Users\admin\Desktop&gt; .duplicateSMTP.PS1 | out-file duplicateItems.txt</pre>
</blockquote>
<p>Boa sorte!</p>
