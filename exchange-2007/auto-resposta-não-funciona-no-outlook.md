# Auto-Resposta não funciona no Outlook

Date: 2014-03-21 18:34:18

Categories: Exchange 2007, Exchange 2010

---

<p>Caso seus usuários utilizam as regras do Outlook para encaminhar automaticamente seus e-mails para um endereço de e-mail externo e mesmo corretamente configuradas, essas regras podem não funcionar e o e-mail encaminhado nunca deixa a sua organização.</p>
<p>Isso ocorre porque no Exchange, por padrão, a mensagem de encaminhamento automático é bloqueada. Para resolver este problema você terá que seguir os passos abaixo:</p>
<p>Abra o Exchange Management Console &gt; Organization Configuration &gt; Hub Transport &gt; Remote Domains tab &gt; Botão direito em Default &gt; Message Format tab<br />
Marque “Allow automatic forward”</p>
<p><a href="http://solucoesms.com.br/wp-content/uploads/2014/03/AllowAutoForward_2k7_2k10.png"><img loading="lazy" decoding="async" class="aligncenter size-medium wp-image-129" alt="AllowAutoForward_2k7_2k10" src="http://solucoesms.com.br/wp-content/uploads/2014/03/AllowAutoForward_2k7_2k10-268x300.png" width="268" height="300" /></a></p>
<p>&nbsp;</p>
<p>Caso queira fazer essa alteração via powershell, siga o seguinte comando:</p>
<p lang="powershell">set-RemoteDomain * -AutoForwardEnabled:$true</p>
<p>Enjoy!</p>
