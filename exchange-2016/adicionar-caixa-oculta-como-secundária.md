# Adicionar caixa oculta como secundária

Date: 2017-03-03 15:00:15

Categories: Exchange 2003, Exchange 2007, Exchange 2010, Exchange 2013, Exchange 2016, Exchange 5.5, Office 365

---

<p style="text-align: justify;">Alguns usuários estavam reclamando que não estavam conseguindo acessar uma caixa compartilhada que é oculta no Exchange Server. Para isso, indiquei uma solução fácil, é necessário apenas utilizar o atributo LEGACYEXCHANGEDN no lugar do campo de caixa secundária. Após a alteração a caixa é adicionada e o problema resolvido.</p>
<p style="text-align: justify;">Isso funciona porque o Outlook realmente usa esse valor e não o nome de conta do usuário para se conectar a uma caixa de correio.</p>
