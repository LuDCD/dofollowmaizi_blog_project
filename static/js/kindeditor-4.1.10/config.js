/**
 * Created by asus on 2016/10/4.
 */

KindEditor.ready(function(K) {
    K.create('textarea[name=content]',{
        width: '800px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor',
    });
});