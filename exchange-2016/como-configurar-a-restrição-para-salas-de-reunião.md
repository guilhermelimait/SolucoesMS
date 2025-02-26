# Como configurar a restrição para salas de reunião

Date: 2018-04-19 13:55:42

Categories: Exchange 2013, Exchange 2016, Office 365

---


<p>Já comentei há alguns posts atrás sobre como verificar as restrições de uma sala de reunião, agora, se precisar adicionar a restrição, é preciso executar um comando bem simples, veja só:</p>



<pre class="wp-block-verse">Get-Mailbox saladereuniao@dominio.com.br | Set-CalendarProcessing -AllBookInPolicy:$false -AllRequestInPolicy:$false -BookInPolicy ("user1@dominio.com.br","user2@dominio.com.br")</pre>



<p>Só isso! 🙂</p>



<p>Enjoy!</p>
