# Exportar as regras do outlook de um usuário por powershell

Date: 2018-04-19 14:15:33

Categories: Exchange 2013, Exchange 2016, Office 365

---


<p>Que tal não precisar entrar na máquina do usuário pra verificar quais as regras ele tem criadas em sua conta? Pra isso, faça o seguinte:</p>



<pre class="wp-block-verse">Get-Mailbox usuario@dominio.com.br -ResultSize unlimited | Get-InboxRule -ErrorAction:SilentlyContinue | Select MailboxOwnerID, name, from, redirectto, ForwardTo</pre>



<p>Se precisar de algo mais completo, é só utilizar o seguinte:</p>



<pre class="wp-block-verse">Get-Mailbox usuario@dominio.com.br -ResultSize unlimited | Get-InboxRule -ErrorAction:SilentlyContinue | fl</pre>



<p>Enjoy!</p>
