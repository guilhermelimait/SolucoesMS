# Como bloquear o acesso ao Teams para apenas um usuário?

Date: 2020-11-12 17:37:32

Categories: O365, Office 365, Teams

---

<p>Olá pessoal,<br />
Digamos que por uma definição da área de gestão, alguns usuários precisem ficar sem acesso ao Microsoft Teams, como fazê-lo? Como sabem, à partir do momento que um usuário recebe o licenciamento adequado, ele receberá por padrão o acesso às ferramentas compatíveis, assim como o Teams. Nesse caso, precisamos apenas desabilitar o acesso à essa ferramenta. Veja abaixo:</p>
<p>Via Web:</p>
<p>1- Acesse o portal.office.com</p>
<p>2- Acesse o ambiente de admin.microsoft.com</p>
<p>3- Vá em Usuários &gt; Usuários ativos &gt; digite o nome do usuário que precisa desabilitar o Teams</p>
<p>4- Clique no usuário &gt; Licenças e aplicativos &gt; Desabilite a função de Microsoft Teams:</p>
<p><img loading="lazy" decoding="async" class="aligncenter wp-image-1091 " src="http://solucoesms.com.br/wp-content/uploads/2020/11/2.png" alt="" width="446" height="521" srcset="https://solucoesms.com.br/wp-content/uploads/2020/11/2.png 645w, https://solucoesms.com.br/wp-content/uploads/2020/11/2-256x300.png 256w" sizes="auto, (max-width: 446px) 100vw, 446px" /></p>
<p>Via Powershell:</p>
<p>1- Conecte-se ao seu tenant usando um dos métodos descritos <a href="https://github.com/guilhermelimait/Powershell/tree/master/-%20ConnectO365">aqui</a></p>
<p>2- Execute os seguintes comandos:</p>
<pre>Get-MsolAccountSku

 $acctSKU="&lt;<strong><span style="color: #ff0000;">CompanyName</span></strong>:License&gt; $x = New-MsolLicenseOptions -AccountSkuId $acctSKU -DisabledPlans "TEAMS1"

Get-MsolUser -identity <strong><span style="color: #ff0000;">USUARIO</span> </strong>| Where-Object {$_.licenses[0].AccountSku.SkuPartNumber -eq ($acctSKU).Substring($acctSKU.IndexOf(":")+1, $acctSKU.Length-$acctSKU.IndexOf(":")-1) -and $_.IsLicensed -eq $True} | Set-MsolUserLicense -LicenseOptions $x</pre>
<p>3- Pronto!</p>
<p>Enjoy!</p>
