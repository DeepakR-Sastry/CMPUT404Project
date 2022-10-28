import '../css/PostPopup.scss'
import {useDispatch, useSelector} from "react-redux";
import store, { RootState } from '../store';
import {useHistory} from "react-router";
import { useFormik } from "formik";
import * as Yup from "yup";
import React, { useState } from "react";




const PostPopup = () => {
    const account = useSelector((state: RootState) => state.auth.account);
    const dispatch = useDispatch();
    const history = useHistory();
    const [loading, setLoading] = useState(false);

    // @ts-ignore
    const userId = account?.id;
    const postSource = "TO BE CHANGED LATER/NOT SURE";
    const postOrigin = userId;
    const postCount = 1;
    const postComments = "some comments here"

    // This is used for the post published date
    const current = new Date()
    const date = `${current.getDate()}/${current.getMonth()+1}/${current.getFullYear()}`;

    const handlePostSubmit = (type: string, title: string, source: string, origin: string, 
        description: string, content_type: string, author: string, categories: string, count: number,
        comments: string, published: string, visibility: string, unlisted: boolean) => {
            console.log(type);
            console.log(title);
            console.log(source);
            console.log(origin);
            console.log(description);
            console.log(content_type);
            console.log(author);
            console.log(categories);
            console.log(count);
            console.log(comments);
            console.log(published);
            console.log(visibility);
            console.log(unlisted);
            setLoading(false);
    }

    const formik = useFormik({
        initialValues: {
          post_type: "ASDASDASD",
          post_title: "",
          source: userId,
          origin: userId,
          post_description: "",
          post_content_type: "",
          author: userId,
          post_categories: "",
          count: 0,
          comments: "",
          published: date,
          visibility: "",
          unlisted: false,
        },
        onSubmit: (values) => {
          setLoading(true);
        //   console.log("submitPressed");
          handlePostSubmit(values.post_type, values.post_title, values.source, values.origin, values.post_description, values.post_content_type, values.author, values.post_categories, values.count, values.comments, values.published, values.visibility, values.unlisted);
        },
      });

    return (
        <div className="popUpPost">
            <div className="popUpBox">
                <form onSubmit={formik.handleSubmit}>
                    
                    {/* THIS IS FOR POST TYPE */}
                    <div className="InputField">
                        <div className="InputHeader">
                            Post Type:
                        </div>
                        <input
                            id="post_type" 
                            type="text" 
                            placeholder="Enter Post Type" 
                            name="post_type" 
                            value={formik.values.post_type} 
                            onChange={formik.handleChange} 
                            onBlur={formik.handleBlur}    
                        />
                    </div>
                    {/* THIS IS FOR POST TITLE */}
                    <div className="InputField">
                        <div className="InputHeader">
                            Post Title:
                        </div>
                        <input 
                            id="post_title"
                            type="text"
                            placeholder="Enter Post Title"
                            name="post_title"
                            value={formik.values.post_title}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}   
                        />
                    </div>

                    {/* THIS IS FOR POST DESCRIPTION */}
                    <div className="InputField">
                        <div className="InputHeader">
                            Post Description:
                        </div>
                        <input 
                            id="post_description"
                            type="text"
                            placeholder="Enter Post Description"
                            name="post_description"
                            value={formik.values.post_description}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}   
                        />
                    </div>

                    {/* THIS IS FOR POST CONTENT TYPE */}
                    <div className="InputField">
                        <div className="InputHeader">
                            Content-type
                        </div>
                        <input 
                            id="post_content_type"
                            type="text"
                            placeholder="Enter Post Content Type"
                            name="post_content_type"
                            value={formik.values.post_content_type}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur} 
                        />
                    </div>

                    {/* THIS IS FOR POST CATEGORIES */}
                    <div className="InputField">
                        <div className="InputHeader">
                            Categories
                        </div>
                        <input 
                            id="post_categories"
                            type="text"
                            placeholder="Enter Post Categories"
                            name="post_categories"
                            value={formik.values.post_categories}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur} 
                        />
                    </div>

                    THIS IS FOR POST VISIBILITY
                    <div className="InputField">
                        <div className="InputHeader">
                            Visibility
                        </div>
                        <select 
                            id="visibility" 
                            name="visibility"
                            value={formik.values.visibility}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur} 
                        >
                            <option value="public"> PUBLIC </option>
                            <option value="private"> PRIVATE </option>
                        </select>
                    </div>
                    <div className="submitPost">
                        <button
                            type="submit"
                            disabled={loading}
                        >
                            Create New Post
                        </button>
                    </div>
                </form>
                
            </div>
                
        </div>
    );
};

export default PostPopup;
