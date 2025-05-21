# Comparison Chart

coming soon,,,

# Product Schedule

coming soon,,,

# Personalization overview

大きく取り上げるべき機能として、Personalization 機能があります。
> `A key feature` we want to `highlight` is the Personalization functionality.

Personalization 機能とは、ユーザー一人ひとりの聴力や好みに合わせて、音を最適化する機能のことです。
たとえば聴力の測定結果に基づいて、音のバランスや出力を自動的に調整することで、その人にとって聞きやすい音に仕上げてくれます。
> Personalization `refers to` optimizing the audio output `based on` `each user’s hearing ability` and `personal preferences`.
> For example, the system can `automatically adjust` the `audio balance` and `output level` based on the results of a hearing test, providing sound that is easier for the individual to hear.

様々な Personalization 機能のソリューションベンダが存在しますが、検討の結果、我々は Mimi という企業のソリューションを採用します。
ご存じかと思いますが、PerL1 では Nura のソリューションを用いていましたが、Mimi のソリューションに変わる、ということは大きな変化となります。
> There are various `solution providers` offering Personalization functionality, `and after careful consideration,`
> we have decided to `adopt` the solution provided by a company called Mimi.
> As you may know, the PerL1 previously used a solution from Nura, so switching to Mimi `marks a significant change`.

Mimi がどのようなソリューションなのか、基本的には一般的な Personalization 機能を想像していただければいいかと思います。
より具体的な内容に関しては、ここに添付している各種リンクでご確認いただけます。
> To understand `what Mimi’s solution entails,` `you can generally think of it as a standard personalization feature`.
> For more specific information, please refer to the various links attached here.

次に、App Server Earbuds の関係性がどのように構成されるかについて説明したいと思います。
はじめに、Mimi を採用した Creative のとある製品を引き合いに、App 上の Mimi がどのように動作するのか見ていきたいと思います。
> Next, I would like to explain the relationship between the App, Server, and Earbuds, and how they are structured.
> To begin, let’s `look at` a product from Creative that has adopted Mimi, to understand how Mimi functions within the app.

(ここで、CREATIVE のページに移動し、Flow chart を表示する)

(一番左の画像)

まず、大事な概念として、Personalization 機能には Measurement というステップが必ず必要です。
簡単な Hearing Test を行うことで、個々人の Personalization データを生成するのです。
> One important concept to understand is that any personalization feature requires a Measurement step.
> A simple hearing test `is conducted to` generate personalization data for each individual.

(右の画像に移動)

また、Mimi のソリューションでは、Mimi アカウントが必要です。Denon Headphone App へのサインイン時に、こちらのアカウントへのサインインも行われることを期待しています。
> With Mimi’s solution, `a Mimi account is required`.
> `We expect that when the user signs into the Denon Headphone App, they will also sign into their Mimi account`.

(右下の赤枠の画像に移動)

サインインすると、Measurement がはじまります。方法は 2 通りあって、測定を行うものと、年齢を選択するだけで簡単に設定できるものがあります。
> After signing in, the measurement process `begins`.
> There are two methods: a proper hearing test, and a simplified version where the user just selects their age.

(右の画像に徐々に移動していく)

測定については、このように App のガイダンスに沿って、Earbuds から音を出しながら、どれくらい聞こえたかを App 中の操作で入力する、というものです。
このあたりに関しては、随時この資料を参照してください。Mimi から SDK を渡されるので、その中でこれらの Activity 画面なども含まれているかと思います。
> For the full hearing test, users follow the app’s guidance while sounds are played through the earbuds, and they input what they can hear directly in the app.
> For this process, please refer to the provided documentation.
> Mimi will provide us with an SDK, which likely includes these activity screens.

(一番右の画像に移動)

測定した結果は、このような周波数特性のようなグラフで確認できます。
> The result of the measurement is displayed in a graph resembling a frequency response curve.

(アジェンダのページに戻り、Architecture の章に移る)

今説明した流れの通り、Mimi のソリューションは Earbuds, App, Mimi Server で構成されます。
この図で言うと、Processing Module が Earbuds, Configuration Module が App, Fitting Module が Mimi Server です。
特筆すべきは、Mimi サーバにサインインする必要があるのと、計測データは Mimi Server に渡して Mimi Server 内で計算して Hearing ID という名前の Personalization Data になるということです。
この Mimi Server は、我々の管理するクラウドにホスティングすることはできないです。
> As explained, Mimi’s solution consists of Earbuds, an App, and the Mimi Server.
> In the diagram, the Processing Module corresponds to the earbuds, the Configuration Module to the app, and the Fitting Module to the Mimi server.
> Notably, users must sign in to the Mimi server, and the measurement data is sent to the server, where it is processed and converted into Personalization Data called the Hearing ID.
> This Mimi server cannot be hosted in our own cloud environment.

(Integration Process の章の 1 枚目の画像に移る)

先ほども少し触れましたが、Mimi は Mobile 向けの SDK を用意しています。
> As briefly mentioned earlier, Mimi provides an SDK for mobile platforms.

(Integration Process の章の 2 枚目の画像に移る)

SDK は、Mimi と我々で相互に話を進めて、我々の App のデザインに応じた SDK を提供してもらう、というプロセスとなります。
また、Mimi Server と我々の Server の連携に関しても、同様に Mimi と相談しながら設計を進めていくことになります。
> The SDK will be customized through collaboration between Mimi and us, so that it fits our app’s design.
> Likewise, the server-side integration between the Mimi server and our server will be developed in consultation with Mimi.

# Requests for App team

coming soon,,,
