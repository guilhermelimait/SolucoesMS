# Como exportar os membros de uma lista de distribuição dinâmica no O365?

Date: 2018-03-13 18:28:47

Categories: Exchange, Office 365

---


<p>Olá pessoal,<br />Bem rapidinho apenas pra compartilhar esse script que irá exportar todos os membros de uma DYN DL .</p>



<pre class="wp-block-verse">$DDG = Get-DynamicDistributionGroup "email@dyndl.com"<br /> Get-Recipient -RecipientPreviewFilter $DDG.RecipientFilter | select DisplayName, PrimarySmtpAddress, RecipientType | Export-csv ".\$ddg.csv" -NoTypeInformation</pre>



<p>Enjoy!</p>
