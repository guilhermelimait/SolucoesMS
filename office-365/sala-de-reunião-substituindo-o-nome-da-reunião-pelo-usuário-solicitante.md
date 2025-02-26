# Sala de reunião substituindo o nome da reunião pelo usuário solicitante

Date: 2018-04-06 17:55:28

Categories: Exchange, Office 365

---


<p style="text-align: justify;">Hi everyone!
Como padrão, toda vez que uma sala de reunião é criada no O365, um atributo novo chamado &#8220;-AddOrganizerToSubject&#8221; é criado com o resultado TRUE, substituindo o nome da reunião pelo nome do usuário solicitante. Para corrigir esse problema é simples, basta executar a ação corretiva em cada sala assim como informado abaixo:</p>



<pre class="wp-block-preformatted">Set-CalendarProcessing -Identity room@example.com -AddOrganizerToSubject $false -DeleteSubject $false</pre>




<span style="color: #ff0000;">Observação muito importante: Após a ação acima executada, apenas os novos compromissos terão o seu nome aparecendo, os eventos já agendados não mostrarão devido essa informação já ter sido perdida.</span>

Enjoy!

