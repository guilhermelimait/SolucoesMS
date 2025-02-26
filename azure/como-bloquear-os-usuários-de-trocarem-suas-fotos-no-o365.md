# Como bloquear os usuários de trocarem suas fotos no O365?

Date: 2020-02-03 11:40:52

Categories: Azure, O365

---

<p>Olá pessoal, tudo bem?<br />
Uma nova demanda apareceu onde o cliente gostaria de colocar uma foto padrão no seu O365 para todos os usuários, e dessa forma, apenas eles poderão alterá-la. Os usuários não poderão de forma alguma modificá-la. Querem ver como é fácil fazê-lo?</p>
<p>Para atribuir a política para alguns usuários apenas:</p>
<blockquote><p><span style="color: #ff0000;"><strong>Get-OwaMailboxPolicy -Identity &#8220;OWAPolicy_Name&#8221; | Set-OwaMailboxPolicy -SetPhotoEnabled $false</strong></span></p></blockquote>
<p>Para atribuir a política para todos os usuários da empresa:</p>
<blockquote><p><strong><span style="color: #ff0000;">Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -SetPhotoEnabled $false</span></strong></p></blockquote>
<p>Para atribuir a política para apenas um usuário:</p>
<blockquote><p><strong><span style="color: #ff0000;">Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -SetPhotoEnabled $false -Identity &#8220;nomedousuario&#8221;</span></strong></p></blockquote>
<p>Lembre-se que essa alteração levará até 60 minutos para replicar no seu ambiente.</p>
<p>Enjoy!</p>
