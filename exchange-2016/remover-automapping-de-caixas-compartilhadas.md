# Remover automapping de caixas compartilhadas

Date: 2018-06-18 14:57:39

Categories: Exchange 2013, Exchange 2016, Office 365

---


<p>Automapping é a funcionalidade de abrir caixas de correio compartilhadas quando a caixa do usuário (que tiver o acesso full) for aberta. O único problema disso é que algumas vezes o usuário possui muitos acessos e isso acaba impactando causando lentidão do Outloook. Para desativar essa função, o comando abaixo deve ser executado para cada caixa compartilhada que precisar desativer. Veja a seguir:</p>



<pre class="wp-block-verse">Add-MailboxPermission -Identity caixacompartilhada@dominio.com.br -User usuariocomacesso@dominio.com.br -AccessRights FullAccess -AutoMapping:$false</pre>



<p>Enjoy!</p>
