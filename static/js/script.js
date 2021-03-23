copy = (element) => {
    document.getElementById(element).select();
    document.execCommand("copy");
}
