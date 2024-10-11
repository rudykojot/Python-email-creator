def face_setup():
    html_content = """
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <meta http-equiv="Content-Type" content="text/html; ">
        
        <style type="text/css">
        ReadMsgBody {
        width: 100%;
        }
        
        .ExternalClass {
        width: 100%;
        }
        
        .ExternalClass,
        
        .ExternalClass p,
        
        .ExternalClass span,
        
        .ExternalClass font,
        
        .ExternalClass td,
        
        .ExternalClass div {
        
        line-height: 100%;
        
        }
        
        body {
        
        -webkit-text-size-adjust: 100%;
        
        -ms-text-size-adjust: 100%;
        
        margin: 0 !important;
        
        }
        
        p {
        
        margin: 1em 0;
        
        }
        
        table td {
        
        border-collapse: collapse;
        
        }
        
        img {
        
        outline: 0;
        
        }
        
        a img {
        
        border: none;
        
        }
        </style>
        
        <style type="text/css">
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@500&display=swap');
        
        h1,
        
        h2,
        
        p,
        
        td {
        
        font-family: 'Open Sans', sans-serif;
        
        }
        
        body {
        
        background-color: #efefef;
        
        }
        </style>
        
        <!--[if mso]> <style type="text/css"> /* Begin Outlook Font Fix */ body, table, td { font-family: Arial, Helvetica, sans-serif ; font-size:16px; color:#181818; line-height:1; } /* End Outlook Font Fix */ </style> <![endif]-->
        
        <!-- start:processor:head -->
        
        <!-- start:processor:body:head -->
        
        <style>
        body {
        
        background: #fff0
        }
        
        .a11yHidden {
        
        max-height: 0;
        
        overflow: hidden;
        
        opacity: 0
        }
        
        table.mso {
        
        border-collapse: collapse;
        
        padding: 0;
        
        table-layout: fixed
        }
        
        .sc-box-sizing {
        
        display: inherit
        }
        </style>
        
        <style>
        u+.body .ie-form {
        
        display: block !important
        }
        
        u+.body .ie-formFallback {
        
        display: none !important
        }
        
        u+.body .ie-formFallback {
        
        display: block
        }
        
        u+.body .ie-radio-check {
        
        vertical-align: top;
        
        opacity: .99;
        
        width: auto;
        
        height: auto;
        
        float: left;
        
        border-radius: initial
        }
        
        u+.body .ie-btn {
        
        display: block
        }
        
        u+.body .ie-gmailhide {
        
        display: none !important
        }
        
        noinput {
        
        display: inline !important
        }
        
        .ie-radio-check {
        
        display: inline-block;
        
        opacity: 0;
        
        width: 0;
        
        height: 0;
        
        margin: 0;
        
        margin: 0 0 0 -9999px;
        
        float: left;
        
        position: absolute;
        
        -webkit-appearance: none
        }
        
        #MessageWebViewDiv .ie-radio-check {
        
        display: block
        }
        
        .ie-radio-check:focus+.ie-btn-wrap .ie-btn,
        
        .ie-radio-check:focus+.ie-btn,
        
        .ie-radio-check:focus+.ie-frm-btn,
        
        .ie-rating-group .ie-radio-check:focus+.ie-btn,
        
        .ie-rating-default:focus+.ie-input-group .ie-rating-group>label>.ie-btn-wrap .ie-btn {
        
        outline: Highlight auto 2px;
        
        outline: -webkit-focus-ring-color auto 5px
        }
        
        .ie-btn-wrap,
        
        .ie-frm-btn,
        
        select,
        
        .ie-dropdown-i {
        
        cursor: pointer
        }
        
        .ie-frm-btni {
        
        -webkit-appearance: none;
        
        appearance: none;
        
        border: none;
        
        background: none;
        
        padding: 0;
        
        border-radius: 0
        }
        
        *.ie-input-wraper {
        
        display: block
        }
        
        *.ie-label {
        
        display: block
        }
        
        .ie-b-label,
        
        .ie-btn,
        
        .ie-gmail-btn-wrap {
        
        display: inline-block;
        
        vertical-align: middle;
        
        word-wrap: normal
        }
        
        .ie-b-label-box {
        
        width: 100%;
        
        vertical-align: middle
        }
        
        .ie-input {
        
        display: inline-block;
        
        box-sizing: border-box
        }
        
        .ie-text-in {
        
        font: inherit;
        
        color: inherit;
        
        background: inherit;
        
        border: none;
        
        width: 100%;
        
        height: 100%;
        
        box-sizing: border-box;
        
        vertical-align: top
        }
        
        fieldset {
        
        border: none;
        
        padding: 0;
        
        margin: 0
        }
        
        legend {
        
        width: 100%;
        
        padding: 0;
        
        text-align: inherit
        }
        
        .ie-btn-wrap {
        
        display: inline-block
        }
        
        .ie-btn-label-before {
        
        vertical-align: bottom;
        
        display: inline-block
        }
        
        .ie-btn-label-after {
        
        vertical-align: top;
        
        display: inline-block
        }
        
        .ie-rating-default {
        
        display: none
        }
        
        .ie-rating-default:checked {
        
        display: block
        }
        
        .ie-frm-btn {
        
        display: inline-block;
        
        text-align: center;
        
        font: inherit
        }
        
        *.sc-cadfllm-ic-label-box-sizing {
        
        padding: 15px 0px 5px;
        
        font-weight: bold
        }
        
        *.sc-text-cadfllm-ic-description {
        
        margin: 0px;
        
        padding-top: 5px;
        
        padding-bottom: 5px;
        
        font-size: 12px
        }
        
        *.sc-text-cadfllm-ic-required {
        
        color: #ff0000;
        
        font-weight: bold;
        
        display: inline-block
        }
        
        .sc-link-cadfllm-ic-submit {
        
        margin: 15px 0px;
        
        padding: 15px 10px;
        
        color: #ffffff;
        
        text-decoration: none;
        
        background: #ff8300;
        
        border-radius: 4px
        }
        
        .sc-block-cadfllm-ic-radio-checkbox-label {
        
        display: inline
        }
        
        *.sc-cadfllm-ic-radio-checkbox-label-box-sizing {
        
        font-size: 14px
        }
        
        *.sc-cadfllm-ic-automatic-fallback-section-box-sizing {
        
        text-align: center
        }
        
        .ie-input-cadfllm-ic-text-select {
        
        width: 100%;
        
        max-width: 100%
        }
        
        .ie-input-cadfllm-ic-text-select .ie-text-in {
        
        height: 30px;
        
        border: 1px solid #cccccc
        }
        
        .ie-input-cadfllm-ic-textarea {
        
        width: 100%;
        
        max-width: 100%
        }
        
        .ie-input-cadfllm-ic-textarea .ie-text-in {
        
        height: 80px
        }
        
        u+.body .ie-frm-btni {
        
        font: inherit;
        
        color: inherit;
        
        opacity: 1;
        
        width: auto;
        
        height: auto;
        
        float: none
        }
        
        u+.body .ie-frm-btn {
        
        display: none
        }
        
        u+.body .ie-frm-btni-cadfllm-ic-submit,
        
        *.ie-frm-btn-cadfllm-ic-submit {
        
        width: auto;
        
        margin: 15px 0px;
        
        padding: 15px 10px;
        
        color: #ffffff;
        
        text-decoration: none;
        
        background: #ff8300;
        
        border-radius: 4px
        }
        
        u+.body .ie-frm-btni {
        
        background-image: linear-gradient(transparent, transparent)
        }
        
        *.ie-btn-wrap-cadfllm-ic-radio-checkbox {
        
        display: block
        }
        
        .ie-btn-cadfllm-ic-radio-checkbox,
        
        .ie-r-btn-cadfllm-ic-radio-checkbox,
        
        input:checked+.ie-input-group .ie-r-btn-cadfllm-ic-radio-checkbox,
        
        input:checked+.ie-btn-wrap+label .ie-r-btn-cadfllm-ic-radio-checkbox {
        
        width: 15px;
        
        height: 15px;
        
        margin: 2px 4px 2px 0;
        
        border: 1px solid #cccccc
        }
        
        #rebel label div:hover~* .ie-r-btn-cadfllm-ic-radio-checkbox {
        
        width: 15px !important;
        
        height: 15px !important;
        
        margin: 2px 4px 2px 0;
        
        border: 1px solid #cccccc !important
        }
        
        .ie-btn-cadfllm-ic-radio,
        
        .ie-r-btn-cadfllm-ic-radio,
        
        input:checked+.ie-input-group .ie-r-btn-cadfllm-ic-radio,
        
        input:checked+.ie-btn-wrap+label .ie-r-btn-cadfllm-ic-radio {
        
        border-radius: 50%
        }
        
        #rebel label div:hover~* .ie-r-btn-cadfllm-ic-radio {
        
        border-radius: 50%
        }
        </style>
        
        <style>
        #interactive:checked+#rebel .ie-form {
        
        display: block !important
        }
        
        #interactive:checked+#rebel .ie-formFallback {
        
        display: none
        }
        
        #MessageWebViewDiv #rebel#rebel .ie-form,
        
        .edo-email-view #rebel#rebel .ie-form,
        
        .edo #rebel#rebel .ie-form,
        
        #msgBody #rebel#rebel .ie-form,
        
        .netease_mail_readhtml #interactive:checked+#rebel .ie-form,
        
        .c17637 #interactive:checked+#rebel .ie-form {
        
        display: none !important
        }
        
        #MessageWebViewDiv #rebel#rebel .ie-formFallback,
        
        .edo-email-view #rebel#rebel .ie-formFallback,
        
        .edo #rebel#rebel .ie-formFallback,
        
        #msgBody #rebel#rebel .ie-formFallback,
        
        .netease_mail_readhtml .ie-formFallback,
        
        .netease_mail_readhtml #interactive:checked+#rebel .ie-formFallback,
        
        .c17637 #interactive:checked+#rebel .ie-formFallback {
        
        display: block !important
        }
        
        input:checked+.ie-btn-wrap .ie-btn-cadfllm-ic-radio-checkbox,
        
        input:checked+.ie-btn-cadfllm-ic-radio-checkbox,
        
        #rebel input:checked+.ie-btn-wrap .ie-r-btn-cadfllm-ic-radio-checkbox,
        
        .ie-r-btn-cadfllm-ic-radio-checkbox {
        
        background-color: #6bcdf0
        }
        </style><noscript>
        
        <style>
        #interactive:checked+#rebel .ie-form {
        
        display: none !important
        }
        
        #interactive:checked+#rebel .ie-formFallback {
        
        display: block !important
        }
        </style>
        
        </noscript><!-- end:processor:body:head -->
        
        <!-- end:processor:head -->
        
        <div class="moz-text-html" lang="x-unicode">
        
        <style type="text/css">
        div.preheader {
        
        display: none !important;
        
        }
        </style>
        
        <div class="preheader" style="font-size: 1px; display: none !important;">%%_PreHeader%%</div>
        
        <!-- start:processor:prepend -->
        
        <!-- start:processor:body:prepend -->
        
        <!--[if mso]><!--><input type="radio" name="limited" id="interactive" style="display:none;mso-hide:all;"
        checked="checked">
        
        <!--<![endif]-->
        
        <div id="rebel">
        
        <!-- end:processor:body:prepend -->
        
        <!-- end:processor:prepend -->
        
        <table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
        
        <tbody>
        
        <tr>
        
        <td valign="top" align="center">
        
        </td>
        
        </tr>
        
        <tr>
        
        <td align="center">
        
        <table class="container" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
        
        <tbody>
        
        <tr>
        
        <td>
        
        <!-- added the border style here -->
        
        <table class="tb_properties border_style" width="100%" cellspacing="0"
        cellpadding="0" bgcolor="#ffffff">
        
        <!-- end of comment -->
        
        <tbody>
        
        <tr>
        
        <td valign="top" align="center">
        
        <table width="100%" cellspacing="0" cellpadding="0" border="0"
        align="left">
        
        <tbody>
        
        <tr>
        
        <!-- added padding here -->
        
        <td class="content_padding"
        style="padding:7px;border:0px;">
        
        <!-- end of comment -->
        
        <table width="100%" cellspacing="0"
        cellpadding="0" border="0">
        
        <tbody>
        
        <tr>
        
        <td class="header" role="banner"
        aria-label="header"
        valign="top" align="left">
        
        <table role="presentation"
        style="border-bottom: 1px solid #AEAEAE; min-width: 100%; "
        class="slot-styling"
        width="100%"
        cellspacing="0"
        cellpadding="0">
        
        <tbody>
        
        <tr>
        
        <td style="padding-bottom: 10px; "
        class="slot-styling camarker-inner">
        
        <table
        role="presentation"
        style="min-width: 100%; "
        class="stylingblock-content-wrapper"
        width="100%"
        cellspacing="0"
        cellpadding="0">
        
        <tbody>
        
        <tr>
        
        <td
        class="stylingblock-content-wrapper camarker-inner">
        
        <table
        role="presentation"
        width="100%"
        cellspacing="0"
        cellpadding="0">
        
        <tbody>
        
        <tr>
        
        <td
        align="center">
        
        <img data-assetid="28787"
        src="https://img.freepik.com/free-photo/analog-landscape-city-with-buildings_23-2149661456.jpg?w=2000&t=st=1713595919~exp=1713596519~hmac=998bfccfa89af5102ed4c731f0cf0b85e2875adcf8362f6e26f7c05d6d9caf2a"
        alt=""
        style="display: block; padding: 0px; text-align: center; height: auto; width: 100%; border: 0px;"
        shrinktofit="true"
        width="2000">
        
        </td>
        
        </tr>
        
        </tbody>
        
        </table>
        
        </td>
        
        </tr>
        
        </tbody>
        
        </table>
        
        </td>
        
        </tr>
        
        </tbody>
        
        </table>
        
        </td>
        
        </tr>
    """

    return html_content
